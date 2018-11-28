#!/usr/bin/env python
# coding=utf-8
from __future__ import print_function
from sys import stdin
from collections import defaultdict

def solveCase(caseNumber):
    res = 0
    robot = {'O':(0,1), 'B':(0,1)}
    buttons = zip(*[iter(stdin.readline().split()[1:])]*2)
    for r, b in buttons:
        b = int(b)
        #print((r, b))
        time, button = robot[r]
        res += 1+max(0, abs(b-button)-(res-time))
        robot[r] = (res, b)
    print("Case #{0}: {1}".format(caseNumber, res))

if __name__ == "__main__":
    t = int(stdin.readline())
    for i in range(t):
        solveCase(i+1)
