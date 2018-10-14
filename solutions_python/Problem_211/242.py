from __future__ import division
import sys
sys.stdin = open("input3s.in","r")
sys.stdout = open("output3s.out","w")


test = int(raw_input())
for t in range(test):
    n,k = map(int,raw_input().split())
    u = float(raw_input())
    pi = map(float,raw_input().split())
    pi.sort()
    line = []
    for i in range(n):
        line += [ [pi[i],1] ]
    line += [[1,1]]
    index = 0
    while index<n and u>0:
        if line[index][1]*(line[index+1][0]-line[index][0])<=u:
            line[index+1][1]+=line[index][1]
            u-=(line[index+1][0]-line[index][0])*line[index][1]
            line[index][0]=1###destroying
            line[index][1]=0
        else:
            line[index][0]+=u/line[index][1]
            u=0
        index+=1
    prob=1
    for i in line:
        prob *= (i[0]**i[1]) 
    print "Case #"+str(t+1)+":",
    print("%.9f"%prob)
    
    
            
            
        
        
        
        
    
            
        
