#!/usr/bin/python
from heapq import *
#f=open('testC','r')
f=open('Downloads/C-small-2-attempt3.in','r')
#f=open('Downloads/B-large.in','r')
f.readline()
C=0
for l in f:
    C+=1
    N,K=[int(x) for x in l.split(' ')]
    H=[]
    heappush(H,-N)
    z=Z=0
    if K>3*N/4:
        print  "Case #"+str(C)+":",0,0
        continue
    for i in range(K-1):
        s=-heappop(H)
        if s%2:
            heappush(H,-(s/2))
            heappush(H,-(s/2))
        else:
            heappush(H,-(s/2)+1)
            heappush(H,-(s/2))
    if H:
        s=-heappop(H)
        if s%2:
            Z=z=s/2
        else:
            Z=s/2
            z=s/2-1
    print "Case #"+str(C)+":",Z,z







