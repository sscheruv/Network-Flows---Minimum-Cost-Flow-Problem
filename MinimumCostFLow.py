import numpy as np

#Defining Cost Matrix (Input)
costMatrix = np.matrix('2 2 2 2; 2 2 2 2; 2 2 2 2; 2 2 2 2')

#Supply and demand (Input)
B = np.matrix('8 2 4 6 -5 -5 -7 -3')
supplyNodes = B[B > 0]
demandNodes = B[B < 0]

nSupply = supplyNodes.size
nDemand = demandNodes.size
nTotal = nSupply + nDemand

#Successive Shortest Path Algorithm
flowMatrix = np.tile(0, (nSupply,nDemand)) #define X, Initial Flow
pie = np.repeat(0, nTotal) #define pie, Node Potentials

E = B[B > 0] #Supply Nodes
D = B[B < 0] #Demand Nodes

while E.size != 0 and D.size != 0:    
    #Select l from E and k from D
    l = E[0,0]
    k = D[0,0]
    
    #Setting Distance Labels for all the nodes
    distLabels = np.repeat(0, nTotal)
    for i in range(nSupply):
        distLabels[i] = 0
    for i in range(nDemand):
        label = np.asscalar(min(costMatrix[:, i])[[0]])
        distLabels[i] = label
           
    #updating pie
    pie = pie - distLabels
    
    #flow
    delta = min(l, -k)
    
    #Augment flow (Updating x)
    flowMatrix[nSupply - E.size, nDemand - D.size] = delta
    E[0,0] = E[0,0] - delta 
    D[0,0] = D[0,0] + delta
    
    #Updating E, D    
    if delta == l:
        E = E[:,1:]
    else:
        D = D[:,1:]    
            
print(flowMatrix)
