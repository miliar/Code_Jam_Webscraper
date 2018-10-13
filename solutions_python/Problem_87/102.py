#!/usr/bin/python

import sys, re, string, math

ssr = sys.stdin.readline
ssw = sys.stdout.write
def rdline(): return ssr().strip()
def rdints(): return map(int, ssr().split())



def do_one_case(cnum):
    (X, S, R, t, N) = rdints()
    W = []
    for i in range(N):
        (a, b, c) = rdints()
        W.append((c,b-a))
    no = X - sum([b for (a,b) in W])
    if no: W.append((0,no))
    W.sort()
    assert X == sum([b for (a,b) in W])
    tt = 0.0
    for (a,b) in W:
        tw = b / float(a+S)
        tr = b / float(a+R)
        tr2 = max(0, min(t-tt, tr))
        tw2 = tw * (1.0 - tr2/tr)
        tt += tr2 + tw2
    print "Case #%d: %.8f" % (cnum, tt)


def main():
    N = int(rdline())
    for i in range(N):
        do_one_case(i+1)


if __name__ == "__main__":
    main()
