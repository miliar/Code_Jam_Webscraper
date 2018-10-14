#!/usr/bin/env python
# Python 2.6.5

from itertools import islice, takewhile

t = int(raw_input())

def overlap(i1, i2):
    return ((i1[0] <= i2[0] and i1[1] >= i2[1])
            or (i1[0] >= i2[0] and i1[1] <= i2[1]))

for tc in xrange(1, t+1):
    n = int(raw_input())
    intervals = []
    for _ in xrange(n):
        iv = map(int, raw_input().split())
        ivc = iv[:]
        ivc.sort()
        intervals.append((ivc, iv))
    intervals.sort(lambda x, y: cmp(x, y))
    intervals = map(lambda x: x[1], intervals)
    intersections = 0
    for i in xrange(n):
        iv1 = intervals[i]
        intersections += len(list(takewhile(lambda iv2: overlap(iv1, iv2), islice(intervals, i+1, None))))
    print("Case #%d: %d" % (tc, intersections))
