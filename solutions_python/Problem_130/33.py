#!/usr/bin/python

import sys, re, string, math, fractions, itertools
from fractions import Fraction

ssr = sys.stdin.readline
ssw = sys.stdout.write
def rdline(): return ssr().strip()
def rdstrs(): return ssr.split()
def rdints(): return map(int, ssr().split())



def findmax(N, pos):
    NN = 1<<N
    if pos==-1:
        fm =  -1
    elif pos==NN:
        fm =  NN
    elif pos==0:
        fm =  0
    else:
        assert 1 <= pos < NN
        bn = bin(pos+1)[2:]
        m1 = len(bn) - 1
        fm =  ((1<<m1)-1) << (N-m1)
    #print "findmax(%d,%d) = %d" % (N,pos,fm)
    return fm


def findmin(N, pos):
    NN = 1<<N
    fm = findmax(N, NN-1 - pos)
    fm = NN-1 - fm
    #print "findmin(%d,%d) = %d" % (N,pos,fm)
    return fm



def do_one_case(cnum):
    N, P = rdints()
    NN = 1<<N
    ab = NN - 1
    z = findmax(N, P-1)
    y = findmin(N, P) - 1
    print "Case #%d: %d %d" % (cnum, y, z)


def main():
    N = int(rdline())
    for i in range(N):
        do_one_case(i+1)


if __name__ == "__main__":
    main()
