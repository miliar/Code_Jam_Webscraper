#! /usr/bin/env python

import operator as op

A = {".":0, "0":0, "1":1}
B = {".":0, "0":1, "1":1}

for t in xrange(1, 1 + int(raw_input())):
    N = int(raw_input())
    matrix = []
    wp = []
    a = []
    b = []
    for i in xrange(N):
        row = list(raw_input())
        matrix.append(row)
        a.append(reduce(op.add, map(A.get, row)))
        b.append(reduce(op.add, map(B.get, row)))
        wp.append(float(a[-1]) / b[-1])
    owp = []
    for i in xrange(N):
        num, den = 0, 0
        for j in xrange(N):
            if matrix[j][i] != ".":
                num += float(a[j] - A[matrix[j][i]]) / (b[j] - 1)
                den += 1
        owp.append(num / den if den else 0.0)
    oowp = []
    for i in xrange(N):
        num, den = 0, 0
        for j in xrange(N):
            if matrix[j][i] != ".":
                num += owp[j]
                den += 1
        oowp.append(num / den if den else 0.0)
    print "Case #%d:" % t
    for i in xrange(N):
        rpi = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]
        print "%s" % rpi

# [EOF]
