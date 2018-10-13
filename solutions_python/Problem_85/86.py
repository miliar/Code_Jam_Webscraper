#!/usr/bin/env python
import sys
import math

current = sys.argv[1].split('.')[0]

f = open('%s.in' % current, 'r')
g = open('%s.out' % current, 'w')
lines = f.readlines()
f.close()

def quick(l, t, n, c, inp):
    ret = []
    orig = []
    acce = []
    c = n / c
    for i in range(c + 1):
        ret.extend(inp)
    ret = ret[:n]
    t -= ret[0] * 2
    try:
        while t > 0:
            orig.append(ret.pop(0))
            t -= ret[0] * 2
        else:
            left = -t * 0.5
            orig.append(ret[0] - left)
            ret[0] = left
    except:
        pass
    l = min(l, len(ret))
    for i in range(l):
        m = max(ret)
        acce.append(m)
        ret.remove(m)
    orig.extend(ret)
    ret = sum(orig) * 2 + sum(acce)
    return int(ret)

case = int(lines[0])
cur = 1
for i in range(1, case + 1):
    l = lines[i].split()
    inp = [int(x) for x in l]
    l, t, n, c = inp[:4]
    inp = inp[4:]
    #print 'Case #%d: %d' % (i, quick(l, t, n, c, inp))
    try:
        g.write('Case #%d: %d\n' % (i, quick(l, t, n, c, inp)))
    except:
        print i

g.close()
