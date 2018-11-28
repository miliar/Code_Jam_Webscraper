#!/usr/bin/python

import sys
import functools
import operator
import math
from itertools import chain, combinations
from heapq import heappop, heappush, _siftup


def solve(a, b, k):
    count = 0
    for x in range(a):
        for y in range(b):
            if (x & y) < k:
                count += 1
    return count

def main():
    for i in range(int(raw_input())):
        [a, b, k] = [int(x) for x in raw_input().split()]
        result = solve(a, b, k)
        print ("Case #%s: %s" % (i+1, result))

if __name__ == '__main__':
    main()
