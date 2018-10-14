#! /usr/bin/env python

import random, sys

readline = sys.stdin.readline
for t in xrange(int(readline())):
    readline()
    a = map(int, readline().strip().split(" "))
    print "Case #%d: %.6f" % (t + 1, sum([1 for x in zip(a, sorted(a)) if x[0] != x[1]]))

# [EOF]
