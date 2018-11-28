#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vi:ts=4 sw=4 et

import re
import sys

def read_numbers(input):
    return [ int(x) for x in input.readline().strip().split() ]

def main(input):
    testcases = int(input.readline().strip())
    for testcase in xrange(testcases):
        N, K = read_numbers(input)
        mask = 2**N - 1
        state = 'ON' if mask == K & mask else 'OFF'

        print "Case #%d: %s" % (testcase+1, state)

if __name__ == '__main__':
    main(sys.stdin)
