#!/usr/bin/python

import math


def ReadN(fp):
    return int(fp.readline())


def ReadCase(fp):
    return [int(t) for t in fp.readline().strip().split()]


def SolveCase(r, t):
    a = 2
    b = 1 + 2 * r - 2
    c = -t
    d = b * b - 4 * a * c
    res = (math.sqrt(d) - b) / (2 * a)
    # verify
    res = math.floor(res)
    if 2 * res * (res-1) + res * (1 + 2 * r)>t:
        res = res -1
    return res


def Test(fname):
    resname = fname[:-3] + "_res.txt"
    fp = open(fname)
    fr = open(resname, "wt")
    N = ReadN(fp)
    cnt = 0
    while cnt < N:
        r, t = ReadCase(fp)
        a = SolveCase(r, t)
        result = "Case #%d: %d\n" % (cnt + 1, a)
        fr.write(result)
        cnt = cnt + 1
    fp.close()
    fr.close()


import sys


if __name__ == "__main__":
    fname = sys.argv[1]
    Test(fname)
    print "done."
