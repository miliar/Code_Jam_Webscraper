#! /usr/bin/env python

import sys

for t in xrange(1, 1 + int(raw_input())):
    a = [int(x) for x in raw_input().split()]
    L, tt, N, C = a[:4]
    a = a[4:]
    c = 0
    h = []
    for n in xrange(N):
        h.append(a[n % C] * 2)
    boosted = 0
    for n in xrange(N):
        if (not boosted) and (c + h[n] >= tt):
            dt = tt - c
            c += dt
            h[n] -= dt
            h[n:] = reversed(sorted(h[n:]))
            for l in xrange(L):
                if n + l >= N:
                    break
                h[n + l] /= 2
            boosted = 1
        c += h[n]
    print "Case #%d: %d" % (t, c)

# [EOF]
