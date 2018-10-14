from __future__ import division
import math
input=raw_input()
inp=input.split()
t=inp[0]
inp.pop(0)
#print inp

for i in range(0,len(inp)-1,2):
    r=int(inp[i])
    t=int(inp[i+1])
    #print r,t
    
    k=pow(r+1,2)-pow(r,2)
    #print k
    nc=0
    tp=k
    while tp<=t:
        k+=4
        tp+=k
        nc+=1
    
    print 'Case #%d: %d' % ((i/2)+1, nc)
