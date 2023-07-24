# Two-steps Shapley value computation for Smart Grid management
## Project for Game Theory course at University of Padova.

**Authors**: Lucia Depaoli, Alessandro Fella

We investigate the application of a 2-steps Shapley value in a Smart Grid in order to establish the trading price and to evaluate the total gain/cost for prosumers. A simulation is provided.

**Abstract**: Smart Grid is an electrical grid that allows the management of the resources in an ”intelligent” way. This includes the smart allocation of supplies where it is needed, the trading of energy between consumers that are able to produce electricity (prosumer), the exchange of energy at low-level voltage to minimize the power loss and so on. In this research we use a coalitional game theoretical approach to study the trading price and the coalitions formation of a set of prosumers distributed around a Macro Grid. Our approach works through the computation of two set of Shapley values. The first one is used to establish the trading price in a coalition of prosumers, while the second one is used to evaluate the final gain (for sellers) or cost (for buyers), considering the Smart Grid trading price and the Macro Grid selling and buying price. Lastly, we simulate a simplified real-life scenario using the methods previously exposed.

### Model formulation
Consider a fixed amount of prosumers, each of them connected to a Macro Grid. Each player has a total amount of energy $Q_i = E_i − D_i$, which is the difference between the produced energy $E_i$ and the demand of the house $D_i$. If $Q_i > 0$, then the prosumer is defined as a ”seller”, so she wants to sell the surplus of energy to other houses or to the Macro Grid, in order to make profit. If $Q_i < 0$, the prosumer is a ”buyer” and she needs to satisfy her demand.
We want to understand which are the optimal coalitions and which is the total amount of money a player spends or gains in each configuration.
