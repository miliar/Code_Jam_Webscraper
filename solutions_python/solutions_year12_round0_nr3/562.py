#!/usr/bin/python

import sys
from bisect import bisect_left

def case(A, B):
    cnt = 0
    exp = 1
    pairs = set()
    for n in xrange(A, B+1):
        pairs.clear()
        while n > exp:
            exp *= 10
        x = 10
        y = exp // 10
        while x < exp:
            m = (n % x) * y + n // x
            if m > n and m >= A and m <= B:
                if m not in pairs:
                    pairs.add(m)
                    cnt += 1
            x *= 10
            y //= 10
    return cnt

def main():
    T = int(sys.stdin.readline())
    for x in xrange(1, T+1):
        As, Bs = sys.stdin.readline().split()
        A = int(As)
        B = int(Bs)
        print "Case #%d: %s" % (x, case(A, B))

main()
