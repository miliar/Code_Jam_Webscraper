#! /usr/bin/env python

import sys

for t in xrange(1, 1 + int(raw_input())):
    N, L, H = [int(x) for x in raw_input().split()]
    F = [int(x) for x in raw_input().split()]
    ans = 0
    for j in xrange(L, H + 1):
        no = 0
        for f in F:
            if j % f != 0 and f % j != 0:
                no = 1
                break
        if no == 0:
            ans = j
            break
    if ans == 0:
        print "Case #%d: NO" % t
    else:
        print "Case #%d: %d" % (t, ans)

# [EOF]
