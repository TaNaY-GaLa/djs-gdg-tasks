import random as rn
import numpy as np 
a=int(input("enter the number of rows"))
b=int(input("enter the number of columns"))
forest = np.zeros((a,b))
for i in range(a):
    for j in range (b):
        forest[i][j]=rn.randint(0,1)
print(forest)
zone = np.zeros((3,3))
for i in range (a//2-1,a//2+2):
    for j in range (b//2-1,b//2+2):
        zone[i-a//2+1][j-b//2+1]=forest[i][j]
print("Extraction zone:")
print(zone)
lal= np.sum(zone)
print("Total no. of Lal Chandans in extraction zone:",lal)