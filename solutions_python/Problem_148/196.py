#!/usr/bin/python

import sys
import functools
import operator
import math
from itertools import chain, combinations
from heapq import heappop, heappush, _siftup


def solve(x, files):
    #print x
    #print files
    n = 0
    while files:
        a = files.pop(0)
        for i in range(len(files)):
            if a + files[i] <= x:
                files.pop(i)
                break
        n += 1
    return n

def main():
    for i in range(int(raw_input())):
        [n, l] = [int(x) for x in raw_input().split()]
        files = [int(x) for x in raw_input().split()]
        result = solve(l, sorted(files, reverse=True))
        print ("Case #%s: %s" % (i+1, result))

if __name__ == '__main__':
    main()
