#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import sys

def is_palindrome(number):
    tmp = str(number)
    return tmp == tmp[::-1]

def solve(start, end):
    tmp_start = start ** 0.5
    if tmp_start % 1.0 > 0:
        tmp_start += 1
    tmp_start = int(tmp_start)
    tmp_end = int(end ** 0.5)
    counter = 0

    for number in xrange(tmp_start, tmp_end + 1):
        if is_palindrome(number) and is_palindrome(number ** 2):
            counter += 1

    return counter

def main():
    for case in xrange(int(sys.stdin.readline().strip())):
        print 'Case #%d: %d' % (
            case + 1,
            solve(*map(int, sys.stdin.readline().strip().split(' ')))
        )

    return 0

if __name__ == '__main__':
    sys.exit(main())
