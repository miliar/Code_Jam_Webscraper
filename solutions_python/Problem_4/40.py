#!/usr/bin/python

import sys
rl = sys.stdin.readline

T = int(rl())
for t in xrange(1,T+1):
    n = int(rl())
    v1 = sorted([int(w) for w in rl().split()])
    v2 = sorted([int(w) for w in rl().split()])
    v2.reverse()
    ans = 0
    for (i,j) in zip(v1,v2):
        ans += i * j
    print "Case #%d: %d" % (t, ans)
