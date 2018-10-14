#!/usr/bin/env python
# encoding: utf-8
"""
happy.py

Created by Devin Naquin on 2009-09-11.
Copyright (c) 2009. All rights reserved.
"""

import sys
import os

def read_input(maximum):
    fin = sys.stdin

    test_cases = []

    number = int(fin.readline().strip())
    assert(1 <= number and number <= maximum)

    for i in xrange(number):
        line = fin.readline().strip()

        test_case = map(int, line.split())
        assert(2 <= len(test_case) and len(test_case) <= 3)
        for case in test_case:
            assert(2 <= case and case <=10)

        test_cases.append(test_case)

    assert(number == len(test_cases))
    return test_cases

def happy(number, base, seen = None):
    if not seen:
        seen = {}
    if number in seen:
        return False
    else:
        seen[number] = True

    digits = []
    while number:
        digits.append(number % base)
        number /= base

    result = sum(map(lambda x: x*x, digits))
    return result == 1 or happy(result, base, seen=seen)

def main():
    N = 42

    test_cases = read_input(N)

    for i, case in enumerate(test_cases):

        # compute solution
        n = 2
        while True:
            if reduce(lambda x, y: x and y, [happy(n, base) for base in case]):
                break
            n += 1
        # print solution
        print 'Case #%d: %d' % (i+1, n)

if __name__ == '__main__':
  main()

