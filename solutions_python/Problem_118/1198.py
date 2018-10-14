#!/usr/bin/env python
# coding=utf-8

import sys
from math import sqrt

def ispal(n):
    n = str(n)
    return n == n[::-1]

def solve(A, B):
    #print A, B
    num_pal = 0
    for n in xrange(int(round(sqrt(A))), int(round(sqrt(B))) + 1):
        sqn = n*n
        if ispal(n) and A <= sqn <= B and ispal(sqn):
            #print n, n*n
            num_pal += 1
    return num_pal

def main():
    with open(sys.argv[1]) as f:
        f.readline()
        for i, line in enumerate(f):
            A, B = (int(x) for x in line.strip().split())
            res = solve(A, B)
            print 'Case #%d: %d' % (i+1, res)

if __name__ == "__main__":
    main()
