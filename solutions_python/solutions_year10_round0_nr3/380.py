#!/usr/bin/env python

from sys import stdin

t = int(stdin.readline())
for case in xrange(t):
    r, k, n = [int(x) for x in stdin.readline().split()]
    g = [int(x) for x in stdin.readline().split()]

    qp = 0
    income = 0
    starts = {}
    i = 0
    while i < r:
        if qp in starts:
            dinc = income - starts[qp][0]
            di = i - starts[qp][1]
            m = (r - i - 1) // di
            income += dinc * m
            i += di * m
        else:
            starts[qp] = (income, i)
        riders = 0
        groups = 0
        for group in g[qp:]:
            if riders + group <= k:
                riders += group
                groups += 1
            else:
                break
        else:
            for group in g[:qp]:
                if riders + group <= k:
                    riders += group
                    groups += 1
                else:
                    break
        income += riders
        qp = (qp + groups) % n
        i += 1

    print 'Case #%i: %i' % (case + 1, income)
