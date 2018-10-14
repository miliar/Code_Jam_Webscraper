#!/usr/bin/python3

from common import *

def testcase(x):
    n, m = readintegers()
    a = [0] * n
    for i in range(n):
        a[i] = readintegers()

    row_maxes = [0] * n
    col_maxes = [0] * m
    for i in range(n):
        for j in range(m):
            if a[i][j] > row_maxes[i]:
                row_maxes[i] = a[i][j]
            if a[i][j] > col_maxes[j]:
                col_maxes[j] = a[i][j]

    possible = True
    for i in range(n):
        for j in range(m):
            if a[i][j] < row_maxes[i] and a[i][j] < col_maxes[j]:
                possible = False

    if possible:
        writeline("Case #%d: YES" % x)
    else:
        writeline("Case #%d: NO" % x)

run_tests(testcase)
