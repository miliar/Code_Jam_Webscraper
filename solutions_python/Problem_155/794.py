#!/usr/bin/python
import sys

def getnums(fh):
    return [int(x) for x in fh.readline().split()]

def getstrings(fh):
    return [x for x in fh.readline().split()]

fh = open(sys.argv[1])

t, = getnums(fh)
for i in range(t):
    astr = fh.readline().split()[1:][0]
    a = [d for d in astr]
    total = extra = 0
    for j, c in enumerate(a):
        d = int(c)
        if total < j:
            extra += j - total
        total = max(total, j)
        total += d

    print "Case #%d: %s" % (i+1, extra)
