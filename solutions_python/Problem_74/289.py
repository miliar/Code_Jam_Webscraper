#!/usr/bin/env python

from sys import argv

def solve(v):
    p = [1,1]
    t = [0,0]
    s = 0
    while v:
        x,y = v.pop(0)
        d   = 1+max(0,abs(p[x]-y)-t[x])
        s  += d
        p[x]    = y
        t[x]    = 0
        t[1-x] += d
    return s

f = open(argv[1],'r')
n = int(f.readline())
for x in xrange(n):
    l = f.readline().split()
    w = int(l.pop(0))
    d = {'O':0,'B':1}
    v = []
    for y in xrange(w):
        v.append((d[l.pop(0)],int(l.pop(0))))
    print "Case #%d: %d" % (x,solve(v))
