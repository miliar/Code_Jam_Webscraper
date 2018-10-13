#!/usr/bin/python

import sys, re, string, math, fractions, itertools
from fractions import Fraction

ssr = sys.stdin.readline
ssw = sys.stdout.write
def rdline(): return ssr().strip()
def rdstrs(): return ssr.split()
def rdints(): return map(int, ssr().split())



def do_one_case(cnum):
    N, M = rdints()
    tt1 = 0
    tt2 = 0
    E = []
    for i in range(M):
        o, e, p = rdints()
        k = e - o
        tt1 += p * (N*k - k*(k-1)/2)
        E.append((o,0,p))
        E.append((e,1,p))
    E.sort()
    S = []
    for (s,t,p) in E:
        if t==0:
            S.append([s,p])
        else:
            while p>0:
                o = S[-1][0]
                k = s-o
                if S[-1][1] > p:
                    pp = p
                    S[-1][1] -= p
                else:
                    pp = S[-1][1]
                    del S[-1]
                tt2 += pp * (N*k - k*(k-1)/2)
                p -= pp
    assert not S
    print "Case #%d: %d" % (cnum, (tt1-tt2) % 1000002013)


def main():
    N = int(rdline())
    for i in range(N):
        do_one_case(i+1)


if __name__ == "__main__":
    main()
