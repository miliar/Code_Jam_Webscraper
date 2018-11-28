#!/usr/bin/python

import sys, re, string, math, fractions, itertools
from fractions import Fraction

#Z = 10**9 + 7
ssr = sys.stdin.readline
ssw = sys.stdout.write
sew = sys.stderr.write
def rdline(): return ssr().strip()
def rdstrs(): return ssr().split()
def rdints(): return map(int, ssr().split())
def rd1int(): return int(rdline())



def do_one_case(cnum):
    D, N = rdints()
    t = 0
    for i in range(N):
        K, S = rdints()
        tx = (D-K) / float(S)
        t = max(t,tx)
    s = D/t
    print "Case #%d: %.8f" % (cnum, s)


def main():
    T = rd1int()
    for i in range(T):
        do_one_case(i+1)
        sys.stdout.flush()


if __name__ == "__main__":
    main()
