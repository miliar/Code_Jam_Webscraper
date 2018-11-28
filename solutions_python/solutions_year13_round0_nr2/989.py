#!/usr/bin/env python

import numpy


def mower(lawn):
    nrow, ncol = lawn.shape
    
    if nrow==1 or ncol==1:
        print "Case #%d: YES" % (num)
        return
    
    min_val = 101
    rind = 0
    cind = 0
    for row in range(nrow):
        for col in range(ncol):
            if lawn[row][col]<min_val:
                min_val = lawn[row][col]
                rind = row
                cind = col
    
    row_ok = True
    for i in range(ncol):
        if lawn[rind][i] > min_val:
            row_ok = False
            break

    col_ok = True
    for i in range(nrow):
        if lawn[i][cind] > min_val:
            col_ok = False
            break

    if (not col_ok) and (not row_ok):
        print "Case #%d: NO" % (num)
        return
    else:
        if row_ok:
            lawn = numpy.delete(lawn, rind, 0)
        if col_ok:
            lawn = numpy.delete(lawn, cind, 1)
        mower(lawn)


total = int(raw_input())

for num in xrange(1, total+1):
    nrow, ncol = map(int, raw_input().split())

    lawn = []
    for r in xrange(nrow):
        row = map(int, raw_input().split())
        lawn.append(row)
    lawn = numpy.array(lawn)

    mower(lawn)
    
