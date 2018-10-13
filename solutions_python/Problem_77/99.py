#!/usr/bin/env python

import sys


def foo(ifile):
    n = int(ifile.readline())
    data = [int(x)-1 for x in ifile.readline().split()]
    mask = [0] * n
    res = 0
    for i in range(n):
        if mask[i] != 0:
            continue
        if data[i] == i:
            mask[i] = 1
            continue
        t = i
        mask[i] = 1
        res += 1
        while data[t] != i:
            res += 1
            t = data[t]
            mask[t] = 1
    return "%.6f" % res





def main(ifile, ofile):
    n = int(ifile.readline())
    for i in range(n):
        ofile.write("Case #%s: %s\n" % (i+1, foo(ifile)))

main(sys.stdin, sys.stdout)

