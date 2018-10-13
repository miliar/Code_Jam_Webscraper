#!/usr/bin/env python

import sys
from mpmath import *

mp.dps=300
testcases = int(sys.stdin.readline())
for test in range(1, testcases + 1):
    n = int(sys.stdin.readline())
    print 'Case #%d: %s' % (test, str((3+sqrt(5))**n).split('.')[0].rjust(3, '0')[-3:])
