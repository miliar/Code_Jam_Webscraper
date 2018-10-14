#!/usr/bin/env python

t = int(raw_input())
for case in xrange(1, t + 1):
    # (r, c) = map(int, raw_input().split(' '))
    # cells = []
    # for j in xrange(r):
    #    cells.insert(j, list(raw_input()))
    # done = [[False] * c for _ in range(r)]
    max_t = 0
    (d, n) = map(int, raw_input().split(' '))
    for j in xrange(n):
        (k, s) = map(int, raw_input().split(' '))
        if (k < 0):
            continue
        t = (1.0 * d - k) / s
        max_t = max(max_t, t)
    solution = 1.0 * d / max_t
    print "Case #{0}: {1:.6f}".format(case, solution)
