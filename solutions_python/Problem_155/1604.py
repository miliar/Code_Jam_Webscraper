# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 23:02:46 2015

@author: acl
"""

f = open('/home/acl/Downloads/A-large.in')
out =[]
t = int(f.readline().strip())

for j in range(t):
    N,strin = f.readline().strip().split()
    lis = map(int,list(strin))
    count=0    
    aud = 0
    for i,val in enumerate(lis):
        if val>0:
           if aud<i:        
               temp = i-aud
               
               count +=temp
               aud=i
           aud+=val
        #print aud
    out.append("Case #{}: {}\n".format(j+1,count))          
   # print "##"           
           
f.close()

res = open('/home/acl/Documents/CodeJam/Aout.txt','w')

for val in out:
    res.write(val)
res.close()