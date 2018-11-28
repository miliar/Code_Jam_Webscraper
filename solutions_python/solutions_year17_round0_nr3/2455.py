#!/usr/bin/env pypy

n = int(raw_input())
for t in xrange(1, n + 1):
    n, k = [int(s) for s in raw_input().split(' ')]
    # print n, k
    stalls = [[True, 0, 0]] + [[False, i, n - 1 - i] for i in xrange(n)] + [[True, 0, 0]]
    for _ in xrange(k):
        m = 0
        yep = 0
        for i, stall in enumerate(stalls):
            if stall[0] == False:
                h = min(stall[1:]) + sum(stall[1:]) / 10.0 ** 6
                if h > m:
                    m = h
                    yep = i

        stalls[yep][0] = True

        for i in xrange(stalls[yep][1]):
            stalls[yep - i - 1][2] = i

        for i in xrange(stalls[yep][2]):
            stalls[yep + i + 1][1] = i

    print 'Case #%d: %d %d' % (t, max(stalls[yep][1:]), min(stalls[yep][1:]))
