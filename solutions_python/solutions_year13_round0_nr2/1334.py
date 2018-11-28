#!/usr/bin/python

import sys

BOOL_STR_MAP = {True: "YES", False: "NO"}

def format_test_case(i, n):
    return "Case #%i: %s" % (i+1, BOOL_STR_MAP[n])

def get_ints(line):
    return map(lambda x: int(x), line.strip().split(' '))

def load_lawn(stdin, N, M):
    lawn = []
    for i in xrange(N):
        lawn.append(get_ints(stdin.readline()))
    return lawn

def is_possible(lawn, N, M):
    col_maxs = []
    row_maxs = []
    for row in lawn:
        row_maxs.append(max(row))
    for i in xrange(M):
        col = map(lambda row: row[i], lawn)
        col_maxs.append(max(col))
    for i, row in enumerate(lawn):
        for j, height in enumerate(row):
            if (row_maxs[i] > height
                and col_maxs[j] > height):
                return False
    return True

if __name__=='__main__':
    T = int(sys.stdin.readline())
    for i in xrange(T):
        N, M = get_ints(sys.stdin.readline())
        lawn = load_lawn(sys.stdin, N, M)
        print format_test_case(i, is_possible(lawn, N, M))
