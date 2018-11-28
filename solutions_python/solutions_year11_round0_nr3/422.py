'''
Created on Apr 29, 2011

@author: vipyati
'''
from file.FileOp import *
from decimal import *
import operator
#name = 'B-large-practice'
#name = 'input'
name='C-large'
f = FileRead(name)
o = FileWrite(name)


T= f.INT()
for t in range(T):
    N = f.INT()
    c = []
    tot = 0
    for i in range(N):
        k = f.INT()
        tot = tot+k
        c.append(k)
    le = 0
    lv = 0
    ans = -1
    le = operator.xor(le, c[0]);
    j = 1
    r=0
    while j< len(c):
        r = operator.xor(r, c[j])
        j+=1
    if le!=r:
        o.writeCase(t+1, 'NO')
        continue
    c.sort()
    o.writeCase(t+1,tot-c[0])
    
#
#    
#    
#    for i in range(len(c)-1):
#        le = operator.xor(le, c[i]);
#        lv = lv+c[i]
#        r = 0
#        rv = 0
#        j = i+1
#        while j< len(c):
#            r = operator.xor(r, c[j])
#            rv = rv+c[j]
#            j+=1
#        #print le,r,lv,rv,(lv+rv)
#        if le==r:
#            ans = max(max(lv,rv),ans)
#    
#    if ans == -1:
#        o.writeCase(t+1, 'NO')
#    else:
#        o.writeCase(t+1,ans)
            
            
    
    