#!/usr/bin/python

import sys

from collections import deque

def deceitful_war(x1, x2):
    score = 0
    while len(x1) > 0:
        if x1[0] < x2[0]:
            x1.popleft()
            x2.pop()
        else:
            x1.popleft()
            x2.popleft()
            score += 1

    return score

def war(x1, x2):

    for i in xrange(len(x2)):
        if x1[0] < x2[i]:
            x1.popleft()

    return len(x1)

with open(sys.argv[1], 'r') as f:
    T = int(f.readline().strip())

    for _t in xrange(1, T+1):
        N = int(f.readline().strip())
        x1 = map(float, f.readline().strip().split())
        x2 = map(float, f.readline().strip().split())
        
        a = []
        a.extend(sorted(x1))
        b = []
        b.extend(sorted(x2))

        y = deceitful_war(deque(a), deque(b))

        c = []
        c.extend(sorted(x1))
        d = []
        d.extend(sorted(x2))
        z = war(deque(c), deque(d))

        print 'Case #%d: %d %d' % (_t, y, z)