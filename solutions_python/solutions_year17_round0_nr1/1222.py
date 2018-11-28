#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def row_to_lst(row):
    return [1 if c == '+' else 0 for c in row]


def try_flip(lst, k):
    flips = 0
    for i in xrange(len(lst) - k + 1):
        if lst[i] == 1:
            continue
        for j in xrange(k):
            lst[i+j] = 0 if lst[i+j] else 1
        flips += 1
    if not all(lst[-k:]):
        return 'IMPOSSIBLE'
    return flips


def main():
    cases = int(next(sys.stdin).strip())
    for num in xrange(1, cases+1):
        row, k = next(sys.stdin).strip().split()
        k = int(k)
        print 'Case #{}: {}'.format(num, try_flip(row_to_lst(row), k))


if __name__ == '__main__':
    main()
