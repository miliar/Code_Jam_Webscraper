#!/usr/local/bin/python3.2
from sys import *

n = stdin.readline()
n = int(n)

def R(n, C, F, X):
    ret = X / (2 + n * F)
    for i in range(1, n+1):
        ret += C / (2 + (i - 1) * F)
    return ret

for case in range(1, n+1):
    C, F, X = stdin.readline().split()
    C = float(C)
    F = float(F)
    X = float(X)
    prev = -1
    n = 0
    while True:
        r = R(n, C, F, X)
        n += 1
        if prev == -1:
            prev = r
        else:
            if r > prev:
                print("Case #%d: %.7f" % (case, prev))
                break;
            else:
                prev = r