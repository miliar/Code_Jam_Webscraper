#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def tidy_number(l):
    last_decr = None
    for i in reversed(xrange(1, len(l))):
        if l[i] < l[i-1]:
            l[i-1] -= 1
            last_decr = i-1
    if last_decr is not None:
        for i in xrange(last_decr+1, len(l)):
            l[i] = 9
    return ''.join(map(str, l)).lstrip('0')


def main():
    cases = int(next(sys.stdin).strip())
    for num in xrange(1, cases+1):
        print 'Case #{}: {}'.format(num, tidy_number(map(int, next(sys.stdin).strip())))


if __name__ == '__main__':
    main()
