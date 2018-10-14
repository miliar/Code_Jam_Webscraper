#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==============================================================================
from __future__ import division, unicode_literals

from collections import OrderedDict


def solve():
    """Problem solution implementation."""
    def next_split(length):
        d = (length - 1) / 2
        return [int(round(d)), int(d)]

    n, k = [int(x) for x in raw_input().split()]

    # optimization
    if k == n:
        return '0 0'

    c = OrderedDict({n: 1})
    while c.viewkeys() and k > 1:
        k -= 1
        length = c.iterkeys().next()  # First key == largest key
        new_keys = filter(lambda x: x > 0, next_split(length))
        for nk in new_keys:
            if nk in c:
                c[nk] += 1
            else:
                c[nk] = 1
        # Delete obsolete keys to save memory
        c[length] -= 1
        if c[length] == 0:
            del c[length]

    l_r = next_split(c.iterkeys().next())
    return '{} {}'.format(max(l_r), min(l_r))


# ==============================================================================
if __name__ == '__main__':
    test_cases = int(raw_input())
    for t in xrange(1, test_cases + 1):
        print('Case #{}: {}'.format(t, solve()))
