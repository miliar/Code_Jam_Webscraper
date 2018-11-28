#!/usr/bin/env python

import sys
from itertools import combinations, izip
from collections import Counter, defaultdict
from math import sqrt

T = int(sys.stdin.readline())
for testcase in xrange(T):
    [r,t] = map(int,sys.stdin.readline().split())
    c = 2*r - 1
    result = int((sqrt(8*t+c**2) - c)/4)
    #might be off by 1, so check
    if 2*result**2 + c*result > t:
        result -= 1
    print 'Case #'+str(testcase+1)+':',
    print str(result)
