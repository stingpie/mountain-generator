

import numpy

import matplotlib.pyplot as plt

import random


pnum=80 #number of points
psize=10 # maximum size of point radiuses
matrix=numpy.zeros((64,64)) # heightmap
plates=numpy.zeros((3,pnum)) # array for all the points. 
plates[0,0]=32
plates[1,0]=32


def randsign():
    return 1 if random.random() < 0.5 else -1

for i in range(pnum):
    # generates a point, and moves it randomly relative to the last generated point
    plates[0,(i+1)%pnum]= plates[0,i]+int(random.random()*psize*randsign())
    plates[1,(i+1)%pnum]= plates[1,i]+int(random.random()*psize*randsign())
    plates[2,(i+1)%pnum]= int(random.random()*psize)

                
for x in range(64):
    for y in range(64):
        touching=[]
        for i in range(pnum): #figures out if any of the radiuses overlap. 
            if ((x-plates[0,i])**2+(y-plates[1,i])**2)**(1/2)<=plates[2,i]:
                touching=numpy.append(touching,int(i))
        temp=0
        if len(touching)>=2:
            temp=1
            for i in range(len(touching)):
                
                z=int(touching[i])
                temp*=((x-plates[0,z])**2+(y-plates[1,z])**2)**(1/2)+1 # multiply the heightmap square by the distances of all overlaping points
                
        matrix[x,y]=numpy.arctan((temp**(1/2))/100)/1.57 #normalize results



plt.imshow(matrix) # show the heightmap
plt.colorbar()
plt.show()
