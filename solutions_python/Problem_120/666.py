#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import sys
import math


def area(r):
    outter = r + 1
    return (outter * outter) - (r * r)

def solve(r, t):
    c = 0
    while 1:
        use = area(r)
        if use > t:
            break
        t -= use
        r += 2
        c += 1
    return c


def main():
    for case in xrange(int(sys.stdin.readline().strip())):
        r, t = map(int, sys.stdin.readline().strip().split(' '))
        print 'Case #%d: %d' % (case + 1, solve(r, t))

    return 0

if __name__ == '__main__':
    sys.exit(main())
