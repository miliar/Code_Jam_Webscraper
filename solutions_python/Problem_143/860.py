#!/usr/bin/env python

import sys

if 'xrange' in dir(__builtins__):
    range_ = xrange
else:
    range_ = range

def getl():
    return sys.stdin.readline().strip()

T = int(getl())

for i in range(T):
    x = i + 1

    A, B, K = map(int, getl().split())

    ctr = 0

    for a in range_(A):
        for b in range_(B):
            if (a & b) < K:
                ctr += 1

    # print('Case #%i: %s %s %s' % (x, a, b, k))
    print('Case #%i: %s' % (x, ctr))


