#!/usr/bin/env python

import sys
import math
from decimal import Decimal

f = open(sys.argv[1], 'r')

num_cases = int(f.readline())

for i in range(num_cases):
    r, t = map(Decimal, f.readline().split())
    m = Decimal.sqrt(4*r*r - 4*r + 8*t + 1)
    n = (Decimal(1) - 2*r + m)/4
    print "Case #%d: %d" % (i+1,n)
