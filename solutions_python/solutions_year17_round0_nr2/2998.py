#!/usr/bin/env python

import sys

n_tests = input()
for test_no in xrange(1, n_tests + 1):
    #n = map(int, raw_input())
    n = int(raw_input())
    index = 10
    while index <= n:
        cur_digit = (n / index) % 10
        next_digit = (n * 10 / index) % 10
        if next_digit < cur_digit:
            n = n - (n % index) - 1
        index *= 10
    print 'Case #{0}: {1}'.format(test_no, n)
