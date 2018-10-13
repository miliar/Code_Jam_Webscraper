#!/usr/bin/python3
__author__ = 'Tianren Liu'

import sys
import numpy as np

def allq(S):
    for s in S:
        if s != '?':
            return False
    return True

def line(L):
    res = ""
    slack = 0
    last = ""
    for l in L:
        if l == '?':
            slack += 1
        else:
            last = l
            res += l * (slack+1)
            slack = 0
    return res + last * slack

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for t in range(1,T+1):
        R = int(sys.stdin.readline().split()[0])
        cake = [sys.stdin.readline()[:-1] for _ in range(R)]

        print("Case #{}:".format(t))
        slack = 0
        lastline = ""
        for r in cake:
            l = line(r)
            if l == "":
                slack += 1
            else:
                lastline = l
                for _ in range(slack+1):
                    print(l)
                slack = 0
        for _ in range(slack):
            print(line(lastline))
