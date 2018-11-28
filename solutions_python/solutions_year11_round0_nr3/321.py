#!/usr/bin/env python
import sys

current = sys.argv[1].split('.')[0]

f = open('%s.in' % current, 'r')
g = open('%s.out' % current, 'w')
lines = f.readlines()
f.close()

def padd(x, y):
    return x^y

def more(n, l):
    l = [int(x) for x in l[:n]]
    s = (sum(l), reduce(padd, l))
    if s[1]:
        return 'NO'
    else:
        ret = s[0] - min(l)
        return ret #if ret*2 > s[0] else 'NO'

case = int(lines[0])
for i in range(1, case + 1):
    #print 'Case #%d: %s' % (i, more(int(lines[2*i-1]), lines[2*i].split(' ')))
    g.write('Case #%d: %s\n' % (i, more(int(lines[2*i-1]), lines[2*i].split(' '))))

g.close()
