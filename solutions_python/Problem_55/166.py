#!/usr/bin/env python

import sys
imax = int(sys.stdin.readline())
data = (map(int, line.split()) for line in sys.stdin)

i = 0
while (i < imax):
    i += 1
    R, K, N = data.next()
    G = data.next()
    n = 0
    s = 0
    for r in xrange(R):
        k = K
        m = N
        while (G[n] <= k) and (m > 0):
            s += G[n]
            k -= G[n]
            m -= 1
            n += 1
            n %= N
    print 'Case #%i: %i' % (i, s)
