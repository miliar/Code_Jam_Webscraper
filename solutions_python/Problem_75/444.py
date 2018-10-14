#!/usr/bin/env python
# coding=utf-8
from __future__ import print_function
from sys import stdin
from collections import defaultdict

def solveCase(caseNumber):
    res = []
    case = stdin.readline().split()
    combine = {}
    c = int(case[0])
    for i in range(c):
        cmb = case[1+i]
        combine[cmb[:2]] = cmb[2]
        combine[cmb[1]+cmb[0]] = cmb[2]
    d = int(case[1+c])
    opposed = set()
    for i in range(d):
        opp = case[2+c+i]
        opposed.add(opp)
        opposed.add(opp[1]+opp[0])
    for c in case[-1]:
        if res:
            cmb = res[-1]+c
            if cmb in combine:
                res.pop()
                res.append(combine[cmb])
                continue
            else:
                for r in res:
                    if r+c in opposed:
                        res = []
                        break
                if not res:
                    continue
        res.append(c)
    print("Case #{0}: [{1}]".format(caseNumber, ", ".join(res)))

if __name__ == "__main__":
    t = int(stdin.readline())
    for i in range(t):
        solveCase(i+1)
