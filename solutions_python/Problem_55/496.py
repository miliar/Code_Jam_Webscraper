#!/usr/bin/env python

import array
import sys
from collections import deque

# compute result
def result(R, K, N, l):
    l = [ int(x) for x in l ]
    d = deque(l)

    y = 0
    for i in xrange(0, R):
        nb = 0
        j = N
        d_tmp = []
        while (j > 0):
            e = d.pop()
            nb = nb + e
            if (nb > K):
                nb = nb - e
                d.append(e)
                break
            else:
                d_tmp.append(e)
                j = j - 1
        d.extendleft(d_tmp)
        y = y + nb

    return (y)

# nb tests
C = int(raw_input())
sys.stderr.write(str(C) + " test to compute\n")

# process tests
for x in xrange(1, C+1):
    sys.stderr.write("Load input of test " + str(x) +  "...\n")
    (R, K, N) = raw_input().split(" ")
    R = int(R)
    K = int(K)
    N = int(N)
    l = raw_input().split(" ")
    l.reverse()

    y = result(R, K, N, l)
    print "Case #" + str(x) + ": " + str(y)
