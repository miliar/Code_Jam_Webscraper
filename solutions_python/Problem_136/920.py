#!/usr/bin/env python
# encoding: utf-8

from __future__ import division

import sys

def counter():
    n = 0
    while True:
        yield n
        n += 1

def dbuy(c, f, x, N=2):
    # 30, 1, 2
    cost = None
    ctime = c/N
    cost_tb = [0]
    for i in counter():
        prod = N+f*i
        ctime = cost_tb[-1]
        if cost is None:
            cost = x/prod + ctime
        elif cost >= x/prod + ctime:
            cost = x/prod + ctime
        else:
            break
        cost_tb.append(c/prod+ctime)
    return cost

def main():
    times = int(sys.stdin.readline())
    for case_n in xrange(1, times+1):
        c, f, x = map(float, sys.stdin.readline().split())
        print "Case #%d: %0.7f" % (case_n, dbuy(c, f, x))

if __name__ == "__main__":
    main()
