#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bisect import bisect_left
from bisect import bisect_right
from math import ceil
from math import floor
from math import sqrt


def convert_range(a, b):
    return int(ceil(sqrt(a))), int(floor(sqrt(b)))


def palyndrome(n):
    return str(n) == str(n)[::-1]


def create_index(a, b):
    (a, b) = convert_range(a, b)
    index = []
    for n in xrange(a, b + 1):
        if palyndrome(n) and palyndrome(n * n):
            index.append(n * n)
    return index


def find(a, b, index):
    left = bisect_left(index, a)
    right = bisect_right(index, b) - 1

    if left == right and a <= index[left]:
        return 1
    elif left == right:
        return 0
    else:
        return right - left + 1


def main():
    # index = create_index(1, 10**14)
    index = [1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001,
             1234321, 4008004, 100020001, 102030201, 104060401, 121242121,
             123454321, 125686521, 400080004, 404090404, 10000200001,
             10221412201, 12102420121, 12345654321, 40000800004, 1000002000001,
             1002003002001, 1004006004001, 1020304030201, 1022325232201,
             1024348434201, 1210024200121, 1212225222121, 1214428244121,
             1232346432321, 1234567654321, 4000008000004, 4004009004004]
    for i in xrange(input()):
        a, b = map(int, raw_input().split(' '))
        print 'Case #%d: %d' % (i + 1, find(a, b, index))


if __name__ == '__main__':
    main()
