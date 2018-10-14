#!/usr/bin/env python

import sys

T = int(sys.stdin.readline())
for case in range(T):
    line = [int(x) for x in sys.stdin.readline().split()]
    N, S, p = line[:3]
    line = line[3:]
    assert len(line) == N

    y = 0
    line = sorted(line, reverse=True)
    for total in line:
        r = total % 3
        best = total // 3
        #print total, r, best
        if r == 2:
            best += 1

        if total == 0:
            best = 0
        elif total == 1:
            best = 1
        elif r == 1:
            best += 1
        elif best == (p - 1) and S > 0:
            #print "using an S"
            best += 1
            S -= 1
        #print best
        if best >= p:
            #print "yes"
            y += 1
    print "Case #%i: %s" % (case + 1, y)
