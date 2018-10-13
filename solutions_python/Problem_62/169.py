'''
Created on May 21, 2010

@author: trmcjilt
'''
import sys
from math import sqrt,ceil,floor
filename="A-small-attempt0.in"
#filename="sample.in"
file = open(filename,'r')
sys.stdout = open(filename+".out",'w')


numOfCases = int(file.readline().strip())
caseNum = 1

while numOfCases >= caseNum:

#    rawData = map(int,file.readline().strip().split(' '))  
    T=int(file.readline().strip())
    WireMap = {}
    t = 0
    crosses=0
    while(t<T):
        l1,l2 = map(int,file.readline().strip().split(' '))  
        WireMap[l1]=[l2,l2-l1]
        t+=1
    keys = WireMap.keys()
    keys.sort()
    while len(keys):
        key = keys.pop(0)
        my_val = WireMap[key]
        for restkey in keys:
            restval = WireMap[restkey]
            if restval > my_val:
                break
            else:
                crosses+=1
            
        
    value = crosses
    print "Case #%(caseNum)s: %(value)s"%locals()
    caseNum+=1
    
    
    
    
    