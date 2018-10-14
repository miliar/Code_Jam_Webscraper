#!/usr/bin/env python
# encoding: utf-8
"""
alien.py

Created by Devin Naquin.
Copyright (c) 2009. All rights reserved.
"""

import re
import sys
import os

def read_input(L, D, N):
    fin = sys.stdin


    l, d, n = map(int, fin.readline().strip().split())
    assert(1 <= l and l <= L)
    assert(1 <= d and d <= D)
    assert(1 <= n and n <= N)

    dictionary = []
    for i in xrange(d):
        line = fin.readline().strip()
        assert(len(line) == l)

        dictionary.append(line)

    test_cases = []
    for i in xrange(n):
        line = fin.readline().strip()

        test_cases.append(line)

    assert(n == len(test_cases))
    return dictionary, test_cases

def match(dictionary, pattern):
    # build regex.
    def _paren_to_ors(match):
        return '(%s)' % ('|'.join(list(match.group(0)[1:-1])))
    regex = re.sub(r'\(\w*\)', _paren_to_ors, pattern)

    result = 0
    for word in dictionary:

        match = re.match(regex, word)
        if match:
            if match.group(0) == word:
                result += 1

    return result

def main():
    L, D, N = 15, 5000, 500

    dictionary, test_cases = read_input(L, D, N)

    for i, case in enumerate(test_cases):

        print 'Case #%d: %d' % (i+1, match(dictionary, case))
        
if __name__ == '__main__':
	main()

