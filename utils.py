def shapley_value(n, v):
    seq = [str(i + 1) for i in range(n)]
    All_set = []
    for i in range(n):
        comb = list(itertools.combinations(seq,i + 1))
        All_set.extend(comb)

    new_All_set = ['0']
    for i in range(len(All_set)): 
        s=""
        a = All_set[i]
        for j in a:
            s += j
        new_All_set.append(s)

    zero_set = list(0 for _ in range(len(new_All_set)))

    S = new_All_set
    V = zero_set
    
    for i in range(len(new_All_set)):
        V[i] = v[i]
        
    sv = []
    for i in range(n):
        res = 0
        i_in = [s for s in S if str(i + 1) in s]
        i_not_in = [s for s in S if str(i + 1) not in s]
        for j in range(len(i_in)):
            res += math.factorial(len(i_in[j]) - 1) * math.factorial(n-len(i_in[j])) / math.factorial(n) \
            * (V[S.index(i_in[j])] - V[S.index(i_not_in[j])])
        sv.append(["player"+str(i+1) ,res])
    return sv

def value_function_price(Q, pv, pa):
    Ns = np.where(Q>=0)
    Nb = np.where(Q<0)
    
    ns = np.sum(Q[Q>=0])
    nb = np.sum(Q[Q<0])
    Ep = ns + nb
    Er = -Ep
    v = pa * np.max([0, Ep]) - pv * np.max([0, Er])
    
    return v

def price(subset, energy, pv):

    comb = sum([list(map(list, itertools.combinations(Q, i))) for i in range(len(Q) + 1)], [])
    comb = np.array([np.array(xi) for xi in comb])
    v = []
    
    for i in range(len(comb)):
        v.append(value_function_price(comb[i], 2, 1))
        
    sh = shapley_value(len(Q),v)
    sh = np.array([np.array(xi[1]) for xi in sh])
    idx = np.array(np.where(sh > 0)).reshape(-1)
    
    if len(idx) > 0:
        psm = sum(sh[sh > 0])/sum(np.array([np.array(xi) for xi in v])[idx+1])
    else:
        psm = pv
        
    print('Coalition: ',subset, ' trading price: ',psm)
    return psm

def L_sm_cps(P_req, d):
    
    a = R*d / U0**2
    b = (beta - 1)
    c = P_req
    
    delta = b**2 - 4*a*c
    if delta < 0:
        return (1-beta)*U0**2 / (2*R*d)
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return np.min([x1,x2])
    
def P_loss_cps(P):
    return R*d * P**2 / (U0)**2 + beta*P

def L_sm_sm(P_req, d):
    
    a = R*d / U1**2
    b = -1
    c = P_req
    
    delta = b**2 - 4*a*c
    if delta < 0:
        return U1**2 / (2*R*d)
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        
        return np.min([x1,x2])
    
def P_loss_sm(P, d):
    return R*d * P**2 / (U1)**2

def payoff(subset, Q, energy, psm, u_sell, u):
    Li_cps = 0
    Li_sm = 0
    E_i = Q[Q>=0]
    Q_i = -Q[Q<0]
    
    idx_pos = np.where(energy >= 0)[0]
    idx_neg = np.where(energy < 0)[0]
    
    for i in range(len(idx_pos)-1, -1, -1):
        if all(idx_pos[i] != subset-1):
            idx_pos = np.delete(idx_pos, i, 0)

    for i in range(len(idx_neg)-1, -1,-1):
        if all(idx_neg[i] != subset-1):
            idx_neg = np.delete(idx_neg, i, 0)
            
    
    if all(Q > 0):
        for j in range(len(E_i)):
            u_sell[j] += energy[idx_pos[j]] * pa
        return sum(u_sell)
    

    elif all(Q < 0):
        for i in range(len(Q_i)):
            Li_cps = L_sm_cps(Q_i[i], d[idx_neg[i]])
            u[i] -= Li_cps*pv
        return sum(u)

    else:
        E_i = Q[Q>=0]
        Q_i = -Q[Q<0]
        for i in range(len(Q_i)):
            Li_cps = 0
            Li_sm = 0
            dis = np.sort(distance[idx_neg[i]][idx_pos])
            sort = np.argsort(distance[idx_neg[i],:][subset-1])
            
            Q[Q>0] = E_i
            energy_ordered = Q[sort]
            E_i_aft = energy_ordered[energy_ordered>=0]
            h = 0
            if (E_i != E_i_aft).all():
                u_sell.reverse()
                h = 1
            E_i = E_i_aft

            for j in range(len(E_i)):
                Li_sm = L_sm_sm(Q_i[i], dis[j])
                
                if E_i[j] >= Li_sm:
                    P_loss = P_loss_sm(Li_sm, dis[j])
                    check = float(Q_i[i] - Li_sm + P_loss)
                    E_i[j] -= Li_sm
                    u_sell[j] += Li_sm * psm
                    u[i] -= Li_sm*psm
                    
                    if ((check<= 0.0001) & (check>=-0.0001)):
                        check = 0
                        break
                else:
                    P_loss = P_loss_sm(E_i[j], dis[j])
                    check = float(Q_i[i] - E_i[j] + P_loss)
                    u_sell[j] += E_i[j] * psm
                    E_i[j] = 0
                    u[i] -= E_i[j]*psm
                Q_i[i] = check
                
            if check != 0:
                Li_cps = L_sm_cps(Q_i[i], d[idx_neg[i]])
            
            u[i] -= Li_cps*pv
        for j in range(len(E_i)):
            u_sell[j] += E_i[j] * pa
    if h == 1:
        u_sell.reverse()
    #for i in range(len(E_i)): print('Player: ', idx_pos[i]+1 , ' earns: ', u_sell[i])
    #for i in range(len(Q_i)): print('Player: ', idx_neg[i]+1 , ' pays: ', u[i])
    return sum(u_sell) + sum(u)

def comb(n,k):
    return int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))