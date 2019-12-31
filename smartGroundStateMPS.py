import tensornetwork as tn
import numpy as np
import sys

try:
    
    n = int(input("\nEnter the number of qubits in the system: ")) 

except:
    
    print("\nEnter a positive Integer!")
    sys.exit()

A_beg = tn.Node(np.array([[1.],
                          [0.]]),name = "First")

A_end = tn.Node(np.array([[1., 0.]]),name = "Last")


end = A_beg[1]
Ed = []

Ed.append(A_beg[0])

for i in range(n-2):
    
    a = tn.Node(np.array([[[1.],
                           [0.]]]),name = "Mid")
    end^a[0]
    end = a[2]
    Ed.append(a[1])

end^A_end[0]    
Ed.append(A_end[1])

print("\n")

mps = [j.get_nodes()[0] for j in Ed]

for i,j in enumerate(Ed):
    
    print("The shape of node {0} is {1}.".format(i+1,j.get_nodes()[0].tensor.shape))
    
del A_beg, A_end, a, end, i, j
