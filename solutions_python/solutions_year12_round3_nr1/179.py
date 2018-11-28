#!/usr/bin/env python
import sys
import math

sys.setrecursionlimit(100000000)

current = sys.argv[1].split('.')[0]

f = open('%s.in' % current, 'r')
g = open('%s.out' % current, 'w')
lines = f.readlines()
f.close()

def path(vec, i):
    if not vec[i]:
        yield i
    else:
        for inh in vec[i]:
            p = path(vec, inh)
            for j in p:
                yield j

def diag(vec):
    for i in range(1, len(vec)):
        tmp = []
        p = path(vec, i)
        for j in p:
            if j in tmp:
                return 'Yes'
            else:
                tmp.append(j)
    return 'No'

case = int(lines[0])
cur = 1
for i in range(1, case + 1):
    n = int(lines[cur])
    cur += 1
    vec = [[]]
    for j in range(n):
        vec.append([int(x) for x in lines[cur + j].split()][1:])
    cur += n
    ret = diag(vec)
    #print 'Case #%d: %s' % (i, ret)
    g.write('Case #%d: %s\n' % (i, ret))

g.close()
