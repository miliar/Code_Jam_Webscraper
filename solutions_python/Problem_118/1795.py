#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Description"""

__author__ = 'Pedro Larroy'
__version__ = '0.1'

import os
import sys
import copy
import pprint
pp = pprint.PrettyPrinter(indent=4)


def isqrt(x):
    if x < 0:
        raise ValueError('square root not defined for negative numbers')
    n = int(x)
    if n == 0:
        return 0
    a, b = divmod(n.bit_length(), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y

def readcase(fd):
    (L,U) = map(int, fd.readline().rstrip().split())
    case = (L,U)
    return case

def read_input(fname):
    fd = open(fname, 'rb')
    ncases = int(fd.readline().rstrip())
    cases = []
    for i in range(ncases):
        cases.append(readcase(fd))
    return cases


def is_palindrome(num):
    s = str(num)
    L = len(s)
    N = L - (L // 2)
    for i in range(N):
        if s[i] != s[L-1-i]:
            return False
    return True

def solve(case):
    LO = 0
    HI = 1
    N = 0
    for num in xrange(case[LO], case[HI] + 1):
        if is_palindrome(num):
            sqr = isqrt(num)
            sqr2 = sqr * sqr
            if sqr2 == num and is_palindrome(sqr):
                N += 1
                #print 'yes', num
    return N


def main():
    if len(sys.argv) != 2:
        sys.exit(1)

    fname = sys.argv[1]
    cases = read_input(fname)
#    pp.pprint(cases)
    for (i, case) in enumerate(cases):
        print 'Case #{0}: {1}'.format(i+1, solve(case))

    return 1

if __name__ == '__main__':
    sys.exit(main())

