#!/usr/bin/env python3

from sys import stdin

def NL():
    return stdin.readline()

def calc(C, F, X):
    tsec = X / 2
    ii = 0
    mid = 0
    while True:
        sec = C/2 + mid + X/(2+F+F*ii)
        ii += 1
        mid += C/(2+F*ii)

        if sec < tsec:
            tsec = sec
        else:
            return tsec

def go(tc):
    C, F, X = map(float, NL().split())
    sec = calc(C, F, X)
    print("Case #{}: {:.7f}".format(tc, sec))

TC = int(NL())
for tc in range(1, TC+1):
    go(tc)

