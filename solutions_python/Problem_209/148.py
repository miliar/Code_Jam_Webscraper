#!/usr/bin/env python

from math import pi


def row(fn):
    return map(fn, raw_input().strip().split())


for t in xrange(1, input()+1):
    N, K = row(int)
    P = [row(int) for _ in xrange(N)]
    P.sort(key=lambda (r, h): 2*pi*r*h, reverse=True)

    best = 0

    for idx in xrange(len(P)):
        rb, hb = P[idx]
        p = P[:idx] + P[idx+1:]
        res = pi*(rb**2) + 2*pi*rb*hb

        k = K - 1
        for r, h in p:
            if k > 0 and r <= rb:
                res += 2*pi*r*h
                k -= 1

        best = max(best, res)

    print 'Case #%d: %f' % (t, best)
