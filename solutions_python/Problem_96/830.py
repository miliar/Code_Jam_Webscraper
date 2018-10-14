#!/usr/bin/env python

def numabove(l,z):
    z=max(z,0)
    n=0
    for i in l:
        if i>z:
            n+=1
    return n

T=int(raw_input())
for t in xrange(1,T+1):
    il=map(int,raw_input().split())
    N,S,p=il[:3]
    l=il[3:]
    a,b=numabove(l,3*p-3),numabove(l,3*p-5)
    b-=a
    if p==0:
        a=N
        b=0
    print 'Case #{0}: {1}'.format(t,a+min(b,S))

