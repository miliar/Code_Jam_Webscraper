#!/usr/bin/python
from collections import Counter

def result(num_stalls, num_people):
    gaps = Counter([num_stalls])
    l, r = 0, 0
    for i in range(num_people):
        max_gap = max(gaps)
        #print 'largest gap', max_gap, gaps[max_gap]
        gaps[max_gap] -= 1
        if gaps[max_gap] == 0:
            del gaps[max_gap]
        r = max_gap // 2
        l = max_gap - r - 1
        #print 'split into', r, l
        gaps.update((r, l))
    return r, l

t = int(raw_input())
for case in range(t):
    n, k = raw_input().split()
    n = int(n)
    k = int(k)
    print 'Case #{}: {} {}'.format(case + 1, *result(n, k))
