import tensorflow as tf
import tensornetwork as tn
import numpy as np


n = int(input("\nEnter the number of qubits in the system: "))
g = np.array([1.0,0.0])

#%% Creation of the rank n Ground State Tensor

p = tf.tensordot(g,g,axes = 0)

for i in range (2,n):
    p = tf.tensordot(p,g,axes = 0)
    

Psi = tn.Node(p.numpy())
P = Psi


#print("\n\n Psi is: \n",Psi.tensor,"\n\n")

#%% Repeated SVD for decomposition into MPS

Edges = P.edges
L = []

for i in range (0,n-1):
#    print("\n\n\n",i,"\n\n\n")
    Edges = list(P.get_all_dangling())
    El = list(P.get_all_nondangling()) 
    El.append(Edges[0])
    Er = Edges[1:]
    l,P,_ = tn.split_node(P,El,Er,max_truncation_err = 0.0)
    L.append(l)

L.append(P)

#%% Verification!

t = 1

print("\n\n")
for i in range (1,n-1):
    
    print("The shape of node {0} is {1}.".format(i+1,L[i].tensor.shape))
    M = np.dot(np.transpose(L[i].tensor[:,0,:]),L[i].tensor[:,0,:])
    M = M + np.dot(np.transpose(L[i].tensor[:,1,:]),L[i].tensor[:,1,:])
    if (np.all(np.equal(M, np.eye(M.shape[0])))):
        
        print("Node {} Verified! \n".format(i+1))
        
    else:
        
        print("ERROR!!")
        break
        t = 0
            
print("\n")
    
if (t):
    
    print("Success!")    
    
else:
    
    print("Failed!")
    
    
print("\n")
