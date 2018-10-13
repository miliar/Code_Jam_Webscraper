#!/usr/bin/env python

import sys

def get_max_rows_and_cols(lawn, nrows, ncols):
    row_maxes = [0] * nrows
    for i, row in enumerate(lawn):
        row_maxes[i] = max(row)
    col_maxes = [0] * ncols
    for i, col in enumerate(zip(*lawn)):
        col_maxes[i] = max(col)
    return row_maxes, col_maxes

def valid_lawn(lawn, row_maxes, col_maxes):
    for i, row in enumerate(lawn):
        for j, height in enumerate(row):
            if row_maxes[i] > height and col_maxes[j] > height:
                return False
    return True

def parse_lawns(lawnfile):
    num_lawns = int(lawnfile.readline().strip())

    lawns = []
    for i in range(num_lawns):
        nrows, ncols = map(int, lawnfile.readline().strip().split())
        lawn = []
        for j in range(nrows):
            lawn.append(map(int, lawnfile.readline().strip().split()))
        lawns.append(lawn)

    return lawns

if __name__ == '__main__':
    lawns = parse_lawns(open(sys.argv[1]))
    for i, lawn in enumerate(lawns, start=1):
        row_max, col_max = get_max_rows_and_cols(lawn, len(lawn), len(lawn[0]))
        if valid_lawn(lawn, row_max, col_max):
            print 'Case #%d: YES' % i
        else:
            print 'Case #%d: NO' % i
