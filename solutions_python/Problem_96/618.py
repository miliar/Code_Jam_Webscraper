#!/usr/bin/env python

import sys

cnt_max = int(sys.stdin.readline())
for cnt in xrange(1, cnt_max+1):
    ans = 0
    used_s = 0
    print "Case #%d:" % cnt,
    line = map(int, sys.stdin.readline().rstrip().split())
    N, S, p = line[0:3]
    for t in line[3:3+N]:
        a = t//3
        r = t%3
        best = a if r == 0 else a + 1
        if best >= p:
            ans += 1
        elif (used_s < S) and (best == p-1) and (r == 0 or r == 2) and (t >= 2 and t <= 28):
            ans += 1
            used_s += 1
    print ans
    # used_s < S is no effect to ans, because no negative effect to best
