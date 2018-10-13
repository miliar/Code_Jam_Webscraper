#!/usr/bin/python

from common import *

infinity = 1000001

def solve(p, t, m, d, i):
    arr = [infinity] * p
    if d == 1:
        j = i - (2 ** (p - 1))
        m1 = min(m[j * 2], m[j * 2 + 1])
        if m1 < p:
            arr[m1] = t[i]
        for k in xrange(0, m1):
            arr[k] = 0
        return arr
    else:
        arr1 = solve(p, t, m, d - 1, 2 * i)
        arr2 = solve(p, t, m, d - 1, 2 * i + 1)
        for k in xrange(0, p - 1):
            arr[k] = min(t[i] + arr1[k] + arr2[k], arr1[k + 1] + arr2[k + 1])
        return arr

def testcase(x):
    p = readinteger()
    m = readintegers()
    t = [0] * (2 ** p)
    for i in xrange(0, p):
        ints = readintegers()
        for j in xrange(0, len(ints)):
            t[(2 ** (p - i - 1)) + j] = ints[j]

    arr = solve(p, t, m, p, 1)

    writeline("Case #%d: %d" % (x, arr[0]))

run_tests(testcase)
