#!/usr/bin/env python

import os
import math
import copy

def solveCase(sMax, data, caseNum):
    extras = 0

    clappers = int(data[0])
    for i in range(1, sMax + 1):
        numAtThisLevel = int(data[i])
        if clappers >= i:
            clappers += numAtThisLevel
        else:
            extras += (i - clappers)
            clappers += (i - clappers) + numAtThisLevel

    print "Case #{}: {}".format(caseNum, extras)

def main():
    f = open("A-large.in", "r")
    T = int(f.readline())

    caseNum = 1
    for line in f.readlines():
        line = line.strip()
        case = line.split()
        solveCase(int(case[0]), case[1], caseNum)
        caseNum += 1

main()
