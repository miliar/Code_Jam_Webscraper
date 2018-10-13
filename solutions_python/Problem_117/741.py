#!/usr/bin/python

import os
import sys

fin = sys.stdin

msg_c = 'Case #%d: %s'

UNVERIFIED = 0
IN_VERIFICATION = 1
VERIFIED = 2

def min_max_row(lawn, i):
    i = iter(lawn[i])
    min = i.next()
    max = min
    for h in i:
        if h < min:
            min = h
        if h > max:
            max = h
    return [min, max]

def min_max_col(lawn, j):
    min = lawn[0][j]
    max = min
    for i in xrange(1, len(lawn)):
        h = lawn[i][j]
        if h < min:
            min = h
        if h > max:
            max = h
    return [min, max]

def val_row(lawn, row, uedge, sedge):
    # Determine if verification needs to be done and set state accordingly
    if sedge[row] is not None:
        if sedge[row][1] == VERIFIED:
            return True
        elif sedge[row][1] == IN_VERIFICATION:
            return None
    if sedge[row] is None:
        row_mm = min_max_row(lawn, row)
        if row_mm[0] == row_mm[1]:
            sedge[row] = [row_mm[1], VERIFIED]
            return True
        sedge[row] = [row_mm[1], IN_VERIFICATION]
    else:
        sedge[row][1] = IN_VERIFICATION

    row_h = sedge[row][0]
    # Verify
    for j in xrange(len(lawn[row])):
        h = lawn[row][j]
        if h == row_h:
            # Doesn't matter what height this column is mowed at
            continue
        if uedge[j] is None:
            if val_col(lawn, j, uedge, sedge) == False:
                return False
        # Height must be set by column or not possible
        if h != uedge[j][0]:
            return False

    # Finished verification
    sedge[row][1] = VERIFIED
    return True

def val_col(lawn, col, uedge, sedge):
    # Determine if verification needs to be done and set state accordingly
    if uedge[col] is not None:
        if uedge[col][1] == VERIFIED:
            return True
        elif uedge[col][1] == IN_VERIFICATION:
            return None
    if uedge[col] is None:
        col_mm = min_max_col(lawn, col)
        if col_mm[0] == col_mm[1]:
            uedge[col] = [col_mm[1], VERIFIED]
            return True
        uedge[col] = [col_mm[1], IN_VERIFICATION]
    else:
        uedge[col][1] = IN_VERIFICATION

    col_h = uedge[col][0]
    # Verify
    for i in xrange(len(lawn)):
        h = lawn[i][col]
        if h == col_h:
            # Doesn't matter what height this row is mowed at
            continue
        if sedge[i] is None:
            if val_row(lawn, i, uedge, sedge) == False:
                return False
        # Height must be set by row or not possible
        if h != sedge[i][0]:
            return False

    # Finished verification
    uedge[col][1] = VERIFIED
    return True

def solve(fin):
    N, M = map(int, fin.readline().strip().split())
    lawn = []
    sedge = [None] * N
    uedge = [None] * M
    for i in xrange(N):
        lawn.append(map(int, fin.readline().strip().split()))
    # Validate all rows
    for i in xrange(len(sedge)):
        if val_row(lawn, i, uedge, sedge) == False:
            return 'NO'
    for j in xrange(len(uedge)):
        if val_col(lawn, j, uedge, sedge) == False:
            return 'NO'
    return 'YES'

def main():
    T = int(fin.readline())
    for t in xrange(1, T + 1):
        print msg_c % (t, solve(fin))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fin = open(sys.argv[1], 'r')
    main()
