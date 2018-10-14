import sys
from operator import *
from math import *


f = sys.stdin

t = int(f.readline())
for i in xrange(t):
    n = int(f.readline())
    ss = []
    us = []
    cs = []
    for j in xrange(n):
        x = f.readline().strip()
        ss.append(x)
        l = None
        y = ''
        ct = []
        k = -1
        for c in x:
            if c != l:
                ct.append(1)
                k += 1
                y += c
                l = c
            else:
                ct[k] += 1
        us.append(y)
        cs.append(ct)
        #print y, ct
    
    if len(set(us)) != 1:
        print 'Case #%d: Fegla Won' % (i+1)
        continue
    
    gs = []
    o = 0
    for j in xrange(len(cs[0])):
        items = map(itemgetter(j), cs)
        d = sum(items)
        g = round(d * 1. / n)
        o += sum(map(lambda c: abs(c-g), items))
        gs.append(g)
    #print 'gs', gs, 'o', o
    print 'Case #%d: %d' % (i+1, int(o))
