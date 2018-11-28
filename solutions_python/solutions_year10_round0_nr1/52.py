#!/usr/bin/python

import sys
from math import *

C = int(sys.stdin.readline())

for i in range(C):
    line = sys.stdin.readline().strip().split()
    n = int(line[0])
    k = int(line[1])

    if k - (2**n - 1) >= 0 and (k - (2**n-1)) % 2**n == 0:
        print "Case #%d: ON" % (i+1)
    else:
        print "Case #%d: OFF" % (i+1)
