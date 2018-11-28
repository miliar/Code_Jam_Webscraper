#! /usr/bin/env python

import operator as op, sys

for i in xrange(int(sys.stdin.readline())):
    sys.stdin.readline()
    a = sorted(map(int, sys.stdin.readline().strip().split(" ")))
    print "Case #%d:" % (i + 1), "NO" if reduce(op.xor, a) else sum(a[1:])

# [EOF]
