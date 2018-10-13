#!/usr/bin/env python2
# -*- coding: utf-8 -*-

t= int(raw_input())
for i in xrange(1, t+1):

    n, k= [int(x) for x in raw_input().split()]
    a=[]
    for j in xrange(n):
        a+=[[float(x) for x in raw_input().split()]]
    a.sort()
    a.reverse()
    b=[x+[2*x[0]*x[1]] for x in a]
    c=[2*x[0]*x[1] for x in a]
#    print b
    tans=0.0
    ans=-1.0
    for j in xrange(n-k+1):
        tans=a[j][0]*a[j][0]+2*a[j][0]*a[j][1]
        d=c[j+1:]
        d.sort()
        if k > 1:
            tans+=sum(d[-(k-1):])
        if tans>ans:
            ans=tans
    ans=(ans)*3.1415926535897953
    print "Case #%d: %f" %(i, ans)