#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import OrderedDict

def split(n):
    return (n-1) // 2, n // 2

def solve_new(n, k):
    od = OrderedDict()
    od[n] = 1
    os = None
    while k > 0:
        os = max(od.keys(), key=int)
        slots = od.pop(os)
        k -= slots
        x, y = split(os)
        od[x] = od[x] + slots if x in od else slots
        od[y] = od[y] + slots if y in od else slots

    return ' '.join([str(x) for x in reversed(sorted(split(os)))])


if __name__ == "__main__":
    test_cases = input()

    for i in xrange(1, test_cases+1):
        N, K = [int(x) for x in raw_input().split(" ")]
        print "Case #{}: {}".format(i, solve_new(N, K))
