#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==============================================================================
from __future__ import unicode_literals


def print_solution(i, solution):
    """Print the solution string."""
    print('Case #{}: {}'.format(i, solution))


# ==============================================================================

def clean_unused(p):
    """Remove happy start."""
    while p and p[0]:
        p = p[1:]
    return p


def count_flips(s, k):
    """Count the flips."""
    c = 0
    s = clean_unused(s)
    while s:
        if k > len(s):
            c = -1
            break
        for x in xrange(k):
            s[x] = not s[x]
        c += 1
        s = clean_unused(s)
    return c


def solve():
    """Problem solution implementation."""
    s, k = raw_input().strip().split()
    s = [x == '+' for x in s]
    k = int(k)
    sol = count_flips(s, k)
    return 'IMPOSSIBLE' if sol < 0 else str(sol)


# ==============================================================================
if __name__ == '__main__':
    test_cases = int(raw_input())
    for t in xrange(test_cases):
        solution = solve()
        print_solution(t + 1, solution)
