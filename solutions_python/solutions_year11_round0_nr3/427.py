#!/usr/bin/env python
# coding=utf-8
from __future__ import print_function
from sys import stdin
from collections import defaultdict

def solveCase(caseNumber):
    res = "NO"
    n = int(stdin.readline())
    C = map(int, stdin.readline().split())
    xor = 0
    for c in C:
        xor ^= c
    if xor == 0:
        res = sum(C)-min(C)
    print("Case #{0}: {1}".format(caseNumber, res))

if __name__ == "__main__":
    t = int(stdin.readline())
    for i in range(t):
        solveCase(i+1)
