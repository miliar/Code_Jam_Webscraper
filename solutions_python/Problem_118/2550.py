#!/usr/bin/env python

import sys
from math import sqrt

def pal(x):
    x = str(x)
    return x == x[::-1]

if __name__ == "__main__":
    t = int(sys.stdin.readline())
    for case in range(1, t+1):
        count = 0
        i, j = [long(c) for c in sys.stdin.readline().split(" ")]

        for n in range(i, j+1):
            r = sqrt(n)
            if r - int(r) != 0.0:
                continue
            if pal(n) and pal(int(r)):
                count += 1
        print "Case #%d: %d" % (case, count)
