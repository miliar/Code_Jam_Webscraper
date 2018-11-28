#!/usr/bin/env python

import sys
from numpy import *

testcases = int(sys.stdin.readline())
for test in range(1, testcases + 1):
    n = int(sys.stdin.readline())
    v1 = map(lambda x: int(x), sys.stdin.readline().split())
    v2 = map(lambda x: int(x), sys.stdin.readline().split())
    v1.sort()
    v2.sort()
    minpermu = 0
    while v1 != [] and v1[0] <= 0:
        minpermu += v1.pop(0) * v2.pop()
    while v2 != [] and v2[0] <= 0:
        minpermu += v2.pop(0) * v1.pop()
    for i in v1:
        minpermu += i * v2.pop()
    print "Case #%d: %d" % (test, minpermu)
