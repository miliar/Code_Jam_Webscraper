#!/usr/bin/env python

import sys


def solve(k, c, s):
    step = 0
    for i in xrange(c):
        step += k ** i
    return range(1, step*s+1, step)


def __main__():
    cases_no = int(sys.stdin.readline())
    for case_no in xrange(cases_no):
        [k, c, s] = map(int, sys.stdin.readline().split())

        res = solve(k, c, s)
        print "Case #%d: %s" % (case_no + 1, " ".join(map(str, res)))


__main__()
