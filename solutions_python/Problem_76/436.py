#!/usr/bin/env python
import sys

debug = False
def diff(a,b):
    if a < b: return b - a
    return a - b

line = []
#for l in open('sample', 'r'):
for l in sys.stdin:
    l = l.rstrip('\n')
    line.append(l)

T = int(line[0])

for i in range(T):
    N = int(line[2 * i + 1])
    C = [int(k) for k in line[2 * i + 2].split(' ')]
    s = reduce(lambda a,b:a^b, C)
    if s != 0:
        print 'Case #%d: NO' % (i + 1)
    else:
        C.sort()
        C.pop(0)
        print 'Case #%d: %d' % (i + 1, sum(C))
