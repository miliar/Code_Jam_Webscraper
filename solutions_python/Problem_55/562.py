#!/usr/bin/env python
t=input()
for c in range(t):
    r,k,n=map(int,raw_input().split())
    q=map(int,raw_input().split())
    d=0
    for run in range(r):
        Q=[]
        while q:
            if sum(Q)+q[0]>k:
                break
            Q.append(q.pop(0))   
        d+=sum(Q)
        q+=Q  
    print "Case #%s: %s"%(c+1,d)

