#!/usr/bin/python

import sys, re, string, math, fractions, itertools
from fractions import Fraction

ssr = sys.stdin.readline
ssw = sys.stdout.write
def rdline(): return ssr().strip()
def rdstrs(): return ssr().split()
def rdints(): return map(int, ssr().split())
def rd1int(): return int(rdline())

rule = { "R": "RS", "P": "PR", "S": "SP" }
bst = {}

def do_one_case(cnum):
    N, R, P, S = rdints()
    goal = P*"P" + R*"R" + S*"S"
    tries = best(N)
    t2 = [ t[0] for t in tries if t[1]==goal ]
    if t2:
        print "Case #%d: %s" % (cnum, min(t2))
    else:
        print "Case #%d: IMPOSSIBLE" % (cnum,)


def best(N):
    if N in bst:
        return bst[N]
    NN = 2**N
    B = []
    for t in "RPS":
        x = t
        for i in range(N):
            x = "".join(rule[c] for c in x)
        for i in range(N):
            k = 2**i
            x = "".join([ "".join(sorted([ x[j:j+k], x[j+k:j+2*k]])) for j in range(0,NN,2*k) ])
        y = "".join(sorted(x))
        B.append((x,y))
    bst[N] = B
    return B






def main():
    T = rd1int()
    for i in range(T):
        do_one_case(i+1)
        sys.stdout.flush()


if __name__ == "__main__":
    main()
