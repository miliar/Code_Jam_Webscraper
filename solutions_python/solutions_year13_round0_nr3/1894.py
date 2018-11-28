# -*- coding: utf-8 -*-

from sys import exit, stdin
from math import sqrt, ceil


def count(start, end):
    items = []

    real_start, real_end = int_sqrt(start), int_sqrt(end)

    for x in xrange(real_start, real_end + 1):
        q = x * x
        if q > end:
            break

        if is_palidrom(q) and is_palidrom(x):
            items.append(q)

    return len(items)


def int_sqrt(x):
    return int(ceil(sqrt(x)))


def is_palidrom(x):
    return str(x) == str(x)[::-1]


if __name__ == '__main__':
    T = int(stdin.readline())

    for index in range(T):
        A, B = map(int, stdin.readline().strip().split())

        print 'Case #%d: %d' % (index + 1, count(A, B))

    exit()
