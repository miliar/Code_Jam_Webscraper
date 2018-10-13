#!/user/bin/env python -tt

import sys
import os

T = int(sys.stdin.readline())

for t in xrange(1, T+1):
    print 'Case #%d:' % t,
    N = int(sys.stdin.readline())
    ropes = []
    for n in xrange(N):
        rope = tuple(map(int, sys.stdin.readline().split()))
        ropes.append(rope)
    intercepts = 0
    for n in xrange(N):
        for k in xrange(n+1, N):
            if ropes[n][0] < ropes[k][0] and ropes[n][1] > ropes[k][1]:
                intercepts += 1
            if ropes[n][0] > ropes[k][0] and ropes[n][1] < ropes[k][1]:
                intercepts += 1
    print intercepts