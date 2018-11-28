#!/usr/bin/env python

import array
import math
import sys
import fractions
import copy

# compute result
def result(N, l):
    time_tot = 0

    posA = 1
    posB = 1

    timeA = 0
    timeB = 0

    while (len(l) > 0):
        btn_color = l.pop()
        btn_case = int(l.pop())

        if (btn_color == 'B'):
            time = max(0, abs(btn_case - posB) - timeB) + 1
            time_tot += time
            timeA += time
            timeB = 0
            posB = btn_case
        else:
            time = max(0, abs(btn_case - posA) - timeA) + 1
            time_tot += time
            timeB += time
            timeA = 0
            posA = btn_case

    return time_tot

# nb tests
C = int(raw_input())
sys.stderr.write(str(C) + " test to compute\n")

# process tests
for x in xrange(1, C + 1):
    sys.stderr.write("\n")
    sys.stderr.write("Load input of test " + str(x) +  "...\n")
    l = raw_input().split(" ")
    l.reverse()
    N = int(l.pop())

    y = result(N, l)
    print "Case #" + str(x) + ": " + str(y)
