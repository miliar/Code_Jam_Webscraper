#!/usr/bin/env python

from sys import argv
from operator import itemgetter

def solve(x,s,r,t,wl):
    wl.sort(key=itemgetter(2))
    t0 = t
    dx = x
    for w in wl:
        dx -= w[1]-w[0]
    p   = min(dx,r*t0)
    t0 -= p/float(r)
    dt  = p/float(r) + (dx-p)/float(s)
    for w in wl:
        dx  = w[1]-w[0]
        p   = min(dx,(r+w[2])*t0)
        t0 -= p/float(r+w[2])
        dt += p/float(r+w[2]) + (dx-p)/float(s+w[2])
    return dt
    
f = open(argv[1],'r')
p = int(f.readline())
for y in xrange(p):
    x,s,r,t,n = map(int,f.readline().split())
    wl = []
    for z in xrange(n):
        wl.append(map(int,f.readline().split()))
    print 'Case #%d: %.9f' % (y+1,solve(x,s,r,t,wl))
f.close()
