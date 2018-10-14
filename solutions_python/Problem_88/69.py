#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import itertools


def summ(arr, x1,y1, x2, y2):
    ret = 0
    for x in xrange(x1,x2):
        for y in xrange(y1,y2):
            ret += arr[x][y]
    return ret

def check(sheet, x1, y1, k):
    x2, y2 = x1 + k, y1 + k
    xcoord = 0
    ycoord = 0
    totalm = 0
    for x in xrange(x1, x2):
        for y in xrange(y1, y2):
            if x == x1 and y in (y1, y2-1):
                continue
            elif x == x2 - 1 and y in (y1, y2-1):
                continue
            m = sheet[x][y]
            xcoord += x * m
            ycoord += y * m
            totalm += m
    xcoord /= float(totalm)
    ycoord /= float(totalm)
    #if (x1,y1,k) == (1,1,5):
        #print xcoord, ycoord, x1 + x2 / 2.
    return xcoord == (x1 + x2 - 1) / 2. and ycoord == (y1 + y2 - 1) / 2.

def check1(sheet, x1, y1, k):
    x2, y2 = x1 + k, y1 + k

    xsum1 = summ(sheet, x1, y1, x1 + k/2, y2)
    xsum1 -= sheet[x1][y1]
    xsum1 -= sheet[x1][y2-1]

    xsum2 = summ(sheet, x2 - k/2, y1, x2, y2)
    xsum2 -= sheet[x2-1][y1]
    xsum2 -= sheet[x2-1][y2-1]

    ysum1 = summ(sheet, x1, y1, x2, y1 + k/2)
    ysum1 -= sheet[x1][y1]
    ysum1 -= sheet[x2-1][y1]

    ysum2 = summ(sheet, x1, y2 - k/2, x2, y2)
    ysum2 -= sheet[x1][y2-1]
    ysum2 -= sheet[x2-1][y2-1]

    return xsum1 == xsum2 and ysum1 == ysum2

def generategood(sheet, R, C):
    yield 0
    for x1 in xrange(R):
        for y1 in xrange(C):
            for k in itertools.count(3):
                x2 = x1 + k
                y2 = y1 + k
                if x2 > R or y2 > C:
                    break
                if check(sheet, x1, y1, k):
                    yield k

def getmax(sheet, R, C):
    best = max(generategood(sheet, R, C))
    if best < 3:
        return None
    else:
        return best

def main():
    T = int(sys.stdin.readline())
    for i in xrange(T):
        casenum = i + 1
        R, C, D = map(int, sys.stdin.readline().strip().split())
        sheet = []
        for i in xrange(R):
            line = sys.stdin.readline().strip()
            currow = [r + D for r in map(int,line)]
            assert len(currow) == C
            sheet.append(currow)
        best = getmax(sheet, R, C)
        if best is None:
            print "Case #%d: IMPOSSIBLE" % casenum
        else:
            print "Case #%d: %d" % (casenum, best)

if __name__ == '__main__':
    main()
