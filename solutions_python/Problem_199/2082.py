# -*- coding: utf-8 -*-
"""
Created on Fri Apr 07 19:29:20 2017

@author: Sachin
"""
#-+-+-
f = open("A-large.in")
case = 0
first = True
o = open('out-large.txt','w')
imp = False
for line in f:
    if first:
        first = False
        total = int(line)
        continue
    if case-1==total:
        break
   
    case+=1
    k = int(line.split(' ')[1])
    cakes=[1 if x=='+' else 0 for x in line.split(' ')[0]]    
    cnt = 0    
    for i in range(len(cakes)-k+1):
        #-+-+-
        if not cakes[i]:
            cnt+=1
            cakes[i:i+k] = [not x for x in cakes[i:i+k]]
        
        if all(cakes):
            break
    else:
        imp = True
    
    if imp:
        o.write('Case #'+str(case)+': IMPOSSIBLE\n')
        imp = False
    else:
        o.write('Case #'+str(case)+': '+str(cnt)+'\n')

o.close()
f.close()
            