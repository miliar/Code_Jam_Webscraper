#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Problem 1
# ==============================================================================
from __future__ import division, unicode_literals


def solve():
    """Problem solution implementation."""
    d, k_num = [int(x) for x in raw_input().split()]
    horses = []
    for _ in xrange(k_num):
        horses.append([int(x) for x in raw_input().split()])
    times = [(d - k) / s for k, s in horses]
    return str(d / max(times))


# ==============================================================================
if __name__ == '__main__':
    test_cases = int(raw_input())
    for t in xrange(1, test_cases + 1):
        print('Case #{}: {}'.format(t, solve()))
