#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Problem 1
# ==============================================================================
from __future__ import division, unicode_literals

import math


def circle_area(r):
    return math.pi * r * r


def cylinder_side_area(r, h):
    return 2 * math.pi * r * h


def solve():
    """Problem solution implementation."""
    n, k = [int(x) for x in raw_input().split()]
    pancakes = [[int(x) for x in raw_input().split()] for _ in xrange(n)]

    pancakes = sorted(pancakes, key=lambda x: (-x[0], -x[1]))  # sort by radius

    pancakes_circle_area = [circle_area(p[0]) for p in pancakes]
    pancakes_cylinder_area = [cylinder_side_area(*p) for p in pancakes]

    max_total_area = 0
    for i in xrange(0, n - k + 1):
        area = pancakes_circle_area[i] + pancakes_cylinder_area[i] + \
            sum(sorted(pancakes_cylinder_area[i + 1:], key=lambda x: -x)[:k - 1])

        if area > max_total_area:
            max_total_area = area
    return str(max_total_area)


# ==============================================================================
if __name__ == '__main__':
    test_cases = int(raw_input())
    for t in xrange(1, test_cases + 1):
        print('Case #{}: {}'.format(t, solve()))
