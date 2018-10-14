#!/usr/bin/python

import sys, re, string, math, fractions, itertools
from fractions import Fraction

ssr = sys.stdin.readline
ssw = sys.stdout.write
def rdline(): return ssr().strip()
def rdstrs(): return ssr().split()
def rdints(): return map(int, ssr().split())
def rd1int(): return int(rdline())



def do_one_case(cnum):
    sN, sV, sX = rdstrs()
    N = int(sN)
    V = float(sV)
    X = float(sX)
    R = []
    C = []
    for i in range(N):
        Ri, Ci = map(float, rdstrs())
        R.append(Ri)
        C.append(Ci)
    if X<min(C) or X>max(C):
        #print X-min(C), max(C)-X
        print "Case #%d: IMPOSSIBLE" % (cnum,)
        return
    if N==1:
        print "Case #%d: %.9g" % (cnum, V/R[0])
        return
    if N>2:
        print "Case #%d: N>2" % (cnum,)
        return
    assert N==2
    if C[0]==C[1]:
        print "Case #%d: %.9g" % (cnum, V/sum(R))
        return
    x = (X - C[0])/(C[1] - C[0])
    #print x, X, x*C[1]+(1-x)*C[0]
    t = max(x*V/R[1], (1-x)*V/R[0])
    print "Case #%d: %.9g" % (cnum, t)


def main():
    T = rd1int()
    for i in range(T):
        do_one_case(i+1)
        sys.stdout.flush()


if __name__ == "__main__":
    main()
