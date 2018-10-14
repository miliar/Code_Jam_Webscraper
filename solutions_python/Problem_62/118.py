#!/usr/bin/env python

import sys
inp = sys.stdin


def icps(p, o):
    pa, pb = p
    oa, ob = o

    return ((pa < oa) and (pb > ob)) or ((pa > oa) and (pb < ob))

def go():
    N = int(inp.readline())
    points = []
    for i in xrange(N):
        a, b = map(int, inp.readline().split())
        points.append( (a,b))

    ip = 0

    for i in xrange(N):
        for j in xrange(i+1, N):
            if icps(points[i], points[j]):
                ip += 1

    return ip

T = int(inp.readline())

for i in xrange(1, T+1):
    print 'Case #%d: %d' % (i, go())
