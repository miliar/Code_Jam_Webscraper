#!/usr/bin/python

import sys

tests = int(raw_input())

for test in range(tests):
    n, k, b, t = map(int, raw_input().split())
    xv = zip( map(int, raw_input().strip().split()),
        map(int, raw_input().strip().split())
        )
    swaps = 0
    for x, v in reversed(xv):
        if k == 0:
            break
        # Can it reach the end?
        if float(b-x) / v <= t:
            k -= 1
        else:
            # It's a hinder for the rest of the chickens. Must be removed
            swaps += k

    if k > 0:
        swaps = 'IMPOSSIBLE'

    print 'Case #{0}: {1}'.format(test+1, swaps)
