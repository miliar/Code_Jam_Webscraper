#!/usr/bin/python

import sys
sin = sys.stdin

TEST_CASES = int(sin.readline())
for CASE in range(1, TEST_CASES+1):
    smax, s = sin.readline().strip().split(" ")
    current = 0
    result = 0
    for x in s:
        x = int(x)
        current += x
        if x == 0:
            if current == 0:
                current += 1
                result += 1
        current -= 1
    print "Case #%d: %s" % (CASE, result)
