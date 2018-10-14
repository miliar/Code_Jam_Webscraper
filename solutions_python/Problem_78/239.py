#! /usr/bin/env python

import operator as op

gcd = lambda a, b: a if b == 0 else gcd(b, a % b)

for t in xrange(1, 1 + int(raw_input())):
    N, PD, PG = [int(x) for x in raw_input().split()]
    if (PG in [0, 100] and PD != PG) or (N < 100 / gcd(PD, 100)):
        print "Case #%d: %s" % (t, "Broken")
    else:
        print "Case #%d: %s" % (t, "Possible")

# [EOF]
