import numpy as np
nodes=1000
file=open('graphs/whole.txt','r')
graph=[]
for line in file:
        p=line.split()
        tuple=(int(p[0]),int(p[1]))
        if tuple not in graph:#Not adding multiple edges in graph
                graph.append((int(p[0]),int(p[1])))

print("Number of edges excluding multiple directed edges")
print(len(graph))

#Declare numpy array of size 1000 to store out degree
degree=np.zeros((nodes,), dtype=int)

#Finding out-degree of each node
for i in range(len(graph)):
        degree[graph[i][0]-1]+=1

rows, cols = (nodes, nodes)
M=[]
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(0)
    M.append(col)
#Creating probability transition matrix
for i in range(nodes):
        for j in range(nodes):
                edge=(i,j)
                if edge in graph and degree[i]!=0:
                        M[i][j]=float(1/float(degree[i]))

row,cols=(nodes,1)
A=[]
r_old=[]

#Initializing the rank vector with value 1/N
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(1)
    A.append(col)
    r_old.append(1/nodes)
k=40
beta=0.8

matrix=[]#(1-beta)/nodes*A
for i in range(rows):
        col=[]
        for j in range(cols):
                col.append((1-beta)/nodes)
        matrix.append(col)
#Page Rank Equation
for iteration in range(k):
        r_new=beta*np.dot(M,r_old)
        for i in range(nodes):
                r_new[i]+=matrix[i][0]
        r_old=r_new
n=5
idx = (-r_new).argsort()[:n]
print("Node IDs of top 5 nodes")
print(idx+1)
print("Scores of the top 5 nodes")
for i in idx:
        print(r_new[i])
print("Node IDs of bottom 5 nodes")
print((np.argsort(r_new)[:n])+1)
idx=np.argsort(r_new)[:n]
print("Scores of the bottom 5 nodes")
for i in idx:
        print(r_new[i])
