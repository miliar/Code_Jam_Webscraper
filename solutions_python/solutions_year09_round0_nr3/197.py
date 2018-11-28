#!/usr/bin/env python
# encoding: utf-8
"""
left.py

Created by Devin Naquin on 2009-08-27.
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

        test_cases.append(line)

    assert(number == len(test_cases))
    return test_cases

def occurences(text, phrase):

    if len(phrase) == 1:
        return text.count(phrase)

    first, remaining = phrase[0], phrase[1:]
    if not text or not phrase or not first in text:
        return 0

    if phrase == text:
        return 1

    pivot = text.index(first)+1
    if len(text) == pivot:
        return 0
    else:
        return occurences(text[pivot:], phrase) + occurences(text[pivot:], remaining)

def main():
    N = 100

    test_cases = read_input(N)

    for i, case in enumerate(test_cases):

        # compute solution
        number = occurences(case, 'welcome to code jam')
        if number > 9999:
            number = number % 1000

        print 'Case #%d: %04d' % (i+1, number)
        
if __name__ == '__main__':
	main()

