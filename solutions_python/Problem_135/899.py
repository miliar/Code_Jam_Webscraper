import numpy as np
import os
import random


os.chdir('/Users/gaetan/Desktop/google_code/gcode')
filename = 'input.txt' 
fin=open(filename,'r')
str1=fin.read()

str1 = str1.split("\n")
for k in xrange(0,len(str1)):
    str1[k]=str1[k].split(" ")

n=int(str1[0][0])
answer=[]
mat=[]
for i in xrange(0,n):
    answer.append([int(str1[1+10*i][0]),int(str1[6+10*i][0])])
    mat.append([str1[2+10*i:6+10*i],str1[7+10*i:11+10*i]])
 
output=[]   
for i in xrange(0,n):
    count=i+1
    l1=mat[i][0][answer[i][0]-1]
    l2=mat[i][1][answer[i][1]-1]
    lr=[]
    s=0
    for k in l1:
        for j in l2:
            if int(k)==int(j):
                s+=1
                lr.append(int(k))
    if s==0:
        output.append("Case #{0}: Volunteer cheated!".format(count))
    elif s==1:
        d=lr[0]
        output.append("Case #{0}: {1}".format(count,lr[0]))
    else:
        output.append("Case #{0}: Bad magician!".format(count))


data=open("output1.txt", "w")

for fw in range(0,len(output)):
    data.write(output[fw]+"\n")
    
    
