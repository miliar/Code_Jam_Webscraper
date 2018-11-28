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
    R, C = rdints()
    g = []
    for i in range(R):
        g.append(rdline())
    d = {'^': (-1,0), '>': (0,1), 'v': (1,0), '<':(0,-1)}
    N = 0
    for i in range(R):
        for j in range(C):
            c = g[i][j]
            if c != '.':
                di, dj = d[c]
                ii = i + di
                jj = j + dj
                while 0 <= ii < R and 0 <= jj < C:
                    if g[ii][jj] != '.':
                        break
                    ii += di
                    jj += dj
                if 0 <= ii < R and 0 <= jj< C:
                    continue
                N += 1
                for c in '<>^v':
                    di, dj = d[c]
                    ii = i + di
                    jj = j + dj
                    while 0 <= ii < R and 0 <= jj < C:
                        if g[ii][jj] != '.':
                            break
                        ii += di
                        jj += dj
                    if 0 <= ii < R and 0 <= jj < C:
                        break
                if 0 <= ii < R and 0 <= jj < C:
                    continue
                print "Case #%d: IMPOSSIBLE" % (cnum,)
                return
    print "Case #%d: %d" % (cnum, N)


def main():
    T = rd1int()
    for i in range(T):
        do_one_case(i+1)
        sys.stdout.flush()


if __name__ == "__main__":
    main()
