#!/usr/bin/env python

import sys


def foo(ifile):
    n = int(ifile.readline())
    data = [int(x) for x in ifile.readline().split()]
    res = [0] * 30
    for x in data:
        t = 0
        while x > 0:
            res[t] += x % 2
            x //= 2
            t += 1
    for x in res:
        if x % 2 == 1:
            return 'NO'

    return sum(data) - min(data)


def main(ifile, ofile):
    n = int(ifile.readline())
    for i in range(n):
        ofile.write("Case #%s: %s\n" % (i+1, foo(ifile)))

main(sys.stdin, sys.stdout)

