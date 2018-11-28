#!/usr/bin/python

from common import *

def parse(l):
    k = 0
    for i in xrange(0, len(l)):
        if l[i] == '1':
            k = i
    return k

def testcase(x):
    n = readinteger()
    arr = [0] * n
    for i in xrange(0, n):
        arr[i] = parse(readline())

    swaps = 0
    for i in xrange(0, n):
        for j in xrange(i, n):
            if arr[j] <= i:
                swaps += j - i
                for k in xrange(j, i, -1):
                    arr[k] = arr[k - 1]
                break

    writeline("Case #%d: %d" % (x, swaps))

run_tests(testcase)
