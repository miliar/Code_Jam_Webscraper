# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 17:25:40 2015

@author: acl
"""

f = open('/home/acl/Downloads/D-small-attempt1.in')
out =[]
t = int(f.readline().strip())

for i in range(t):
    X,r,c = map(int,f.readline().strip().split())
    size = r*c    
    if X==1:
        out.append("Case #{}: GABRIEL\n".format(i+1))
    elif X==2:
        if size%X==0:
            out.append("Case #{}: GABRIEL\n".format(i+1))
        else:    
            out.append("Case #{}: RICHARD\n".format(i+1))
    elif X==3:
        if size==X or size%X!=0:
            out.append("Case #{}: RICHARD\n".format(i+1))
        else:
            out.append("Case #{}: GABRIEL\n".format(i+1))
    else:
        if size==X or size==8 or size%X!=0:
            out.append("Case #{}: RICHARD\n".format(i+1))
        else:
            out.append("Case #{}: GABRIEL\n".format(i+1))
            
   
f.close()

res = open('/home/acl/Documents/CodeJam/Cout.txt','w')

for val in out:
    res.write(val)
res.close()