#!/usr/bin/env python2

import sys

def lawns(filename):
    with open(filename) as f:
        cases = int(f.readline())
        lawns = []
        for case in range(cases):
            n, m = map(int, f.readline().split())
            lawn = [map(int, f.readline().split()) for i in range(n)]
            lawns.append(lawn)
    return lawns

def cell_ok(lawn, row, col):
    h = lawn[row][col]
    rowdata = lawn[row]
    row_ok = all(x <= h for x in rowdata)
    coldata = [lawn[i][col] for i in range(len(lawn))]
    col_ok = all(x <= h for x in coldata)
    return row_ok or col_ok

filename = sys.argv[1]
for case, lawn in enumerate(lawns(filename), 1):
    n, m = len(lawn), len(lawn[0])
    if all(cell_ok(lawn, i, j) for i in range(n) for j in range(m)):
        print 'Case #{0}: YES'.format(case)
    else:
        print 'Case #{0}: NO'.format(case)

