import numpy as np
import os
import random


os.chdir('/Users/gaetan/Desktop/google_code/gcode')
filename = 'input3.txt' 
fin=open(filename,'r')
str1=fin.read()

str1 = str1.split("\n")
for k in xrange(0,len(str1)):
    str1[k]=str1[k].split(" ")

n=int(str1[0][0])

pbs=[]
for i in xrange(0,n):
    nbuches=int(str1[1+3*i][0])
    l1=[]
    l2=[]
    for k in xrange(0,nbuches):
        l1.append(float(str1[2+3*i][k]))
        l2.append(float(str1[3+3*i][k]))
    l1.sort()
    l2.sort()
    pbs.append([nbuches,l1,l2])

def nbgain(nbuches,l1,l2):
    g=0
    l1bis=list(l1)
    l2bis=list(l2)
    for j in xrange(0,nbuches):
       for l in xrange(j,nbuches):
           if l1bis[j]<l2bis[l]:
                l2bis[l]=0
                g+=1
                break
    return g


output=[]
for k in xrange(0,n):
    nbuches=pbs[k][0]
    l1=pbs[k][1]
    l2=pbs[k][2]
    g=nbgain(nbuches,l1,l2)
    h=nbgain(nbuches,l2,l1)
    output.append("Case #{0}: {1} {2}".format(k+1,h,nbuches-g))


data=open("output2.txt", "w")

for fw in range(0,len(output)):
    data.write(output[fw]+"\n")
    
    
