#!/usr/bin/env python
import sys
import math

current = sys.argv[1].split('.')[0]

f = open('%s.in' % current, 'r')
g = open('%s.out' % current, 'w')
lines = f.readlines()
f.close()

def minivote(l):
    c = l.pop(0)
    orig = l[:]
    s = sum(l)
    minpoints = s * 2.0 / c
    while max(l) > minpoints:
        l = [x for x in l if x < minpoints]
        c = len(l)
        minpoints = (s + sum(l)) * 1.0 / c
    return ['%.6f' % ((minpoints - x) * 100.0 / s if x < minpoints else 0) for x in orig]

case = int(lines[0])
for i in range(1, case + 1):
    l = lines[i].split()
    l = [int(x) for x in l]
    ret = minivote(l)
    #print 'Case #%d: %s' % (i, ' '.join(ret))
    g.write('Case #%d: %s\n' % (i, ' '.join(ret)))

g.close()
