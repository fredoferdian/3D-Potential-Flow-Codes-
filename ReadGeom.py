# import necessary module
import numpy as np
import pyvista
#______________________________________________________________________________
filename="DCW10_7000.dat"
mylines = []
with open(filename, "r") as myfile:
        for myline in myfile:
            mylines.append(myline)
#______________________________________________________________________________
# Finding the index of nodes and faces
num_lines = sum(1 for line in open(filename))
Node=[]
A=[]
for i in range(0,num_lines-1):
    A.append(mylines[i].split())
    if float(A[i][0])==0:
        ind = i
#______________________________________________________________________________
# Extracting the Nodes Corrdinates
X_coord =[];Y_coord =[];Z_coord =[];
A=[]
for i in range(1,ind):
    A.append(mylines[i].split())
    Node.append(A[i-1][0])
    X_coord.append(A[i-1][1])
    Y_coord.append(A[i-1][2])
    Z_coord.append(A[i-1][3])
for i in range(0,len(X_coord)):
    X_coord[i]=float(X_coord[i])
    Y_coord[i]=float(Y_coord[i])
    Z_coord[i]=float(Z_coord[i])
    
Vertices=np.transpose(np.array([X_coord,Y_coord,Z_coord]))
#______________________________________________________________________________
# Extracting the Faces/Topology
Faces=[]
P1=[];P2=[];P3=[];P4=[];P5=[];
#A=[]
for i in range(ind+1,len(mylines)-1):
    A.append(mylines[i].split())
    P1.append(4)
    #P1.append(A[i-2][0])
    P2.append(A[i-2][0])
    P3.append(A[i-2][1])
    P4.append(A[i-2][2])
    P5.append(A[i-2][3])
for i in range(0,len(P1)):
    P1[i]=int(P1[i])
    P2[i]=int(P2[i])-1
    P3[i]=int(P3[i])-1
    P4[i]=int(P4[i])-1
    P5[i]=int(P5[i])-1  
Faces=np.transpose(np.array([P1,P2,P3,P4,P5]))
Faces = np.hstack(Faces)

Surf = pyvista.PolyData(Vertices, Faces)
Surf.plot()
Surf.plot(scalars=np.arange(len(Vertices)), cpos=[-1, 1, 0.5])