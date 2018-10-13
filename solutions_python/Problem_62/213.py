#!/usr/bin/env python

import sys
import array
from copy import copy

#find the result
def result(N, wires):
    nb = 0
    wires.sort()
    spool = copy(wires)

    for (s1, e1) in spool:
        for (s2, e2) in wires:
            if s1 != s2 or s1 != e2:
                if (s1 < s2 and e1 > e2) or (s1 > s2 and e1 < e2):
                    nb = nb + 1

    return (nb / 2)

#nb tests
C = int(raw_input())
sys.stderr.write(str(C) + " test to compute\n")

#process tests
for x in xrange(1, C+1):
    sys.stderr.write("[" + str(x) +  "]\tLoad.. ")
    N = raw_input()
    N = int(N)

    wires = []
    for y in xrange(N):
        (A, B) = [(int(y)) for y in (raw_input().split(' '))]
        wires.append((A, B))

    sys.stderr.write("Compute.. | ")
    y = result(N, wires)
    print "Case #" + str(x) + ": " + str(y)
