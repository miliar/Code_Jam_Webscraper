#!/usr/bin/env python
import math

p = 'A'
s = 'small-attempt%d' % 1
l = 'large'
current = '%s-%s' % (p, l)

f = open('%s.in' % current, 'r')
g = open('%s.out' % current, 'w')
lines = f.readlines()
f.close()

def state(n, k):
    if not n:
        return True
    t = math.floor(float(k) / pow(2, n - 1))
    return t % 2 and state(n - 1, k)

case = int(lines[0])
for i in range(1, case + 1):
    l = lines[i].split(' ')
    n = int(l[0])
    k = int(l[1])
    #print 'Case #%d: %s\n' % (i, state(n, k))
    g.write('Case #%d: %s\n' % (i, "ON" if state(n, k) else "OFF"))

g.close()
