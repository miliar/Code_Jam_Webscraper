#!/usr/bin/env python

from sys import argv

dinit = {}
dinit.update([(chr(x),0) for x in xrange(65,65+26)])

def solve(r,o,w):
    t,d = '',dinit.copy()
    for x in w:
        t += x
        d[x] += 1
        while r.has_key(t[-2:]):
            d[t[-1]] -= 1
            d[t[-2]] -= 1
            t = t[:-2]+r[t[-2:]]
            d[t[-1]] += 1
        for y in o:
            if d[y[0]] and d[y[1]]:
                t = ""
                d = dinit.copy()
    return t

f = open(argv[1],'r')
n = int(f.readline())
for x in xrange(n):
    l = f.readline().split()
    r,b = {},int(l.pop(0))
    for y in xrange(b):
        p = l.pop(0)
        r[p[0]+p[1]] = r[p[1]+p[0]] = p[2]
    o,b = [],int(l.pop(0))
    for y in xrange(b):
        o.append(l.pop(0))
    b = int(l.pop(0))
    w = l.pop(0)[:b]
    print "Case #%d: [%s]" % (1+x,', '.join(solve(r,o,w)))
