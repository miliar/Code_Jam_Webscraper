#!/usr/bin/env python
#
# code for Google Code Jam
# Wu Zhe (jessewoo@gmail.com)

import sys


def k_subsets_i(n, k):
    if n < 0:
        raise ValueError('n must be > 0, got n=%d' % n)
    if k < 0:
        raise ValueError('k must be > 0, got k=%d' % k)

    if k == 0 or n < k:
        yield set()
    elif n == k:
        yield set(range(n))

    else:
        for s in k_subsets_i(n - 1, k - 1):
            s.add(n - 1)
            yield s
        for s in k_subsets_i(n - 1, k):
            yield s

def k_subsets(s, k):
    s = list(s)
    n = len(s)
    for k_set in k_subsets_i(n, k):
        yield set([s[i] for i in k_set])


def solve_case():
    line = map(int, sys.stdin.readline().split())
    n, a, b, c, d, x_0, y_0, m = line

    points = [(x_0, y_0)]
    x = x_0
    y = y_0
    for i in range(n-1):
        x = (x * a + b) % m
        y = (y * c + d) % m
        points.append((x, y))

    total = 0
    for v_set in k_subsets(points, 3):
        v = list(v_set)
        center_x = ((v[0][0] + v[1][0] + v[2][0]) / 3.0)
        center_y = ((v[0][1] + v[1][1] + v[2][1]) / 3.0)
        if (center_x % 1) == 0 and (center_y % 1) == 0:
            total += 1

    return '%d' % total

def process_all():
    n_case = int(sys.stdin.readline().rstrip())
    for i in range(n_case):
        print 'Case #%d: %s' % (i+1, solve_case())

process_all()
