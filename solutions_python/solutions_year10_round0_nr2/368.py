#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import string

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

def diff(n, years):
    minY = min(years)
    dif = []
    i = 0
    while i < n - 1:
        dif.append(abs(int(years[i + 1]) - abs(int(years[i]))))
        i = i + 1
    curGCD = dif[0]
    i = 1
    while i < n - 1:
        curGCD = gcd(curGCD, dif[i])
        i = i + 1
    return minY, curGCD

if __name__ == '__main__':
#    file = open('B.in', 'r')
#    file = open('B-small-attempt0.in', 'r')
#    file = open('B-small-attempt1.in', 'r')
    file = open('B-large.in', 'r')
    for i, line in enumerate(file):
        line = line.rstrip()
        if i == 0:
            testCase = int(line)
        else:
            iN = int(line.split(" ")[0])
            iYears = [int(item) for item in line.split(" ")[1:]]
            minY, cGCD = diff(iN, iYears)
            leastRecent = minY / cGCD * cGCD - minY
            next = leastRecent
            while(next < 0):
                next += cGCD
            print "Case #" + str(i) + ": " + str(next)
