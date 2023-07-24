# Two-steps Shapley value computation for Smart Grid management
## Project for Game Theory course at University of Padova.

**Authors**: Lucia Depaoli, Alessandro Fella

**Project Summary**: Application of a 2-steps Shapley Value computation in a Smart Grid scenario, in order to establish the trading price and to evaluate the total gain/cost for prosumers.

**Abstract**: Smart Grid is an electrical grid that allows the management of the resources in an ”intelligent” way. This includes the smart allocation of supplies where it is needed, the trading of energy between consumers that are able to produce electricity (prosumer), the exchange of energy at low-level voltage to minimize the power loss and so on. In this research we use a coalitional game theoretical approach to study the trading price and the coalitions formation of a set of prosumers distributed around a Macro Grid. Our approach works through the computation of two set of Shapley values. The first one is used to establish the trading price in a coalition of prosumers, while the second one is used to evaluate the final gain (for sellers) or cost (for buyers), considering the Smart Grid trading price and the Macro Grid selling and buying price. Lastly, we simulate a simplified real-life scenario using the methods previously exposed.

For more information, see the [paper](https://github.com/luciadepaoli/smart-grid-shapley-value/blob/main/Smart_Grid_Depaoli_Fella.pdf).

### Model formulation and variables
Define an amount of prosumers in the variable `n_players`. Then fix the selling and buying price $p_{MG,s}$ and $p_{MG,b}$ in the variables `pv` and `pa`. Then we define the energy for each prosumer in the vector `energy`. If the value is negative, then the prosumer is a buyer, otherwise a seller. 

Variables `U0` and `U1` refers, respectively, to the mean value of the voltage in the process prosumer-MG and to the mean value of the voltage in the process prosumer-prosumer. Variable `R` refers to the resistance of the distribution lines and `\beta` is the coefficient that quantify the power lost in the transformer at the M-G. We consider these values fixed.

Finally, we set the distances between the houses and the M-G in the variable `d`, and the matrix of distances between houses in the variable `distance`.
