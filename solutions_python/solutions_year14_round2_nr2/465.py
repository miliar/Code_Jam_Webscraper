#! /usr/bin/env python -u
# coding=utf-8
import sys

__author__ = 'xl'

if __name__ == "__main__":
    fp = open("B.in")
    # fp = open("B.in.sample")
    # fp = sys.stdin
    sys.stdout = open("B.out", "w")

    T = int(fp.readline())
    for t in range(T):
        a, b, k = map(int, fp.readline().split())
        ret = 0
        for na in range(a):
            for nb in range(b):
                if na&nb < k:
                    ret += 1

        print "Case #%s: %d" % (t + 1, ret)



