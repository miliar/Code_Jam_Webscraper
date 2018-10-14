# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 23:27:29 2017

@author: kprashan
"""


import math
def find_stall(n,k):
    numStages = math.ceil(math.log2(k+1) )
    num = n
    binK = bin(k)
    for i in range(numStages-1):
        if binK[-1] == '0':
            num = math.ceil((num-1)/2)
            
        else :
            num = math.floor((num-1)/2)
        binK = binK[:-1]
    return [math.ceil((num-1)/2), math.floor((num-1)/2)]
    
#file_in = "B-large.in"
#array = []
#with open(file_in) as f :
#    for line in f :
#        array.append(line.rstrip())
        
#for line in array :
#    print(line)  
file_in = "C-small-2-attempt0.in"
array = []
with open(file_in) as f :
    for line in f :
        array.append(line.rstrip())
              
T = int(array[0])
fileOut = open("outC-small2.txt","w")
for i in range(1,T+1):
    n,k = [int(i) for i in array[i].rstrip().split()]
#    print(array[i])
#    print("Case #{}: {}".format(i,array[i].rstrip()))
    y,z = find_stall(n,k)
#    print("Case #{}: {} {}".format(i,y,z))
    print("Case #{}: {} {}".format(i,y,z),file=fileOut)
#    print("Case #{}: {}".format(i,find_tidy(array[i].rstrip())),file=fileOut)
fileOut.close()