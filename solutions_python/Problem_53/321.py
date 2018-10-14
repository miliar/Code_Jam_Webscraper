#!/usr/bin/python

from __future__ import division

import sys

caseCount = int(sys.stdin.readline())

for caseIx in range(caseCount):
    n, k = [int(x) for x in sys.stdin.readline().split(' ')]

    print "Case #%d: %s" % (caseIx + 1, "ON" if (k + 1) % (2 ** n) == 0 else "OFF")
