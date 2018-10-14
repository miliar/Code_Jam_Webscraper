#!/usr/bin/python

from common import *

goal = 'welcome to code jam'
mod = 10000

def testcase(x):
    line = readline()
    counts = [0] * len(goal)
    for c in line:
        for i in xrange(len(goal)):
            if goal[i] == c:
                if i > 0:
                    counts[i] = (counts[i] + counts[i - 1]) % mod
                else:
                    counts[i] += 1
    writeline("Case #%d: %04d" % (x, counts[-1]))

run_tests(sys.argv, testcase)
