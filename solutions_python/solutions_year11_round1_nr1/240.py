#!/usr/bin/env python

from sys import stdin
from fractions import gcd

T = int(stdin.readline())

for CASO in xrange(1,T+1):
    (N, Pd, Pg) = [int(x) for x in stdin.readline().strip().split(" ")]

    if Pg == 100 and Pd < 100:
        print "Case #%d: Broken" % (CASO)
        continue

    if Pg == 0 and Pd > 0:
        print "Case #%d: Broken" % (CASO)
        continue

    if N < 100/gcd(Pd,100):
        print "Case #%d: Broken" % (CASO)
        continue

    print "Case #%d: Possible" % (CASO)
