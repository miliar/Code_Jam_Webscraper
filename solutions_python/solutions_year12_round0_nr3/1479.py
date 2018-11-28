#!/usr/bin/env python2
# we use cat <question> | tr ' ' ',' | recycle.py on a Unix system

from math import log10

def digits(n):
    if n>0:
        return int(log10(n))
    if n == 0:
        return 0
    if n<0:
        return int(log10(-n))

N=input()

for c in xrange(1,N+1):
    s=[]
    (A,B)=input()
    for n in xrange(A,B):
        m=n
        d=digits(n)
        for x in xrange(0,d):
            m=m%10*10**d+m/10
            if m>n and m<=B:
                t=(n,m)
                try:
                    s.index(t)
                except ValueError:
                    s.append(t)
    print "Case #%d: %d" % (c,len(s))
#        for s in xrange(1,len(str(n)))
