#!/usr/bin/env python
import sys

current = sys.argv[1].split('.')[0]

f = open('%s.in' % current, 'r')
g = open('%s.out' % current, 'w')
lines = f.readlines()
f.close()

def seconds(n, l):
    od = []
    for i in range(n):
        od.append((l[2*i], int(l[2*i+1])))
    o = (0, 1)
    b = (0, 1)
    t = 0
    for i in od:
        if i[0] == 'O':
            t = o[0] + max(t - o[0], abs(i[1] - o[1]))
            t += 1
            o = (t, i[1])
        elif i[0] == 'B':
            t = b[0] + max(t - b[0], abs(i[1] - b[1]))
            t += 1
            b = (t, i[1])
    return t

case = int(lines[0])
for i in range(1, case + 1):
    l = lines[i].split(' ')
    n, l = int(l[0]), l[1:]
    #print 'Case #%d: %d' % (i, seconds(n, l))
    g.write('Case #%d: %d\n' % (i, seconds(n, l)))

g.close()
