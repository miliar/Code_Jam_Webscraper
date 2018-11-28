#!/usr/bin/env python

import math
import sys
import itertools
from pprint import pprint

def cycles(x):
    a = x

    # count # of digits
    digits = 0
    while a > 0:
        a = math.floor(a / 10)
        digits += 1

    #print(x, digits)

    a = x
    while x > 0:
        r = x % 10
        a = math.floor(a / 10)
        a += r * (10 ** (digits - 1))
        yield a
        x = math.floor(x / 10)

def count_recycles(A, B):
    unique_set = set()

    for i in range(A, B+1):
        if i < 10: continue

        for c in cycles(i):
            if c > i and c <= B:
                unique_set.add((i, c))

    return len(unique_set)

def recycler():
    count = int(sys.stdin.readline())
    #for i in cycles(12345): print(i)

    #cycles(1)
    #cycles(10)
    #cycles(101)
    #cycles(10001)
    #cycles(99999)
    #cycles(100000)
    #cycles(199991)
    #cycles(190900)

    for i in range(count):
        [A, B] = list(map(int, sys.stdin.readline().strip().split()))
        c = count_recycles(A, B)
        print('Case #%d: %d' % (i+1, c))

    #pprint(db)
    #pprint(tr(sample[0][0], db))


if __name__ == '__main__':
    recycler()
