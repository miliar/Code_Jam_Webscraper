#!/usr/bin/python

# vim: set expandtab shiftwidth=4 tabstop=4:

import sys

def solve(data, n, m):
    row_max = []
    col_max = []
    for i in range(n):
        row_max.append(max(data[i]))
    for j in range(m):
        col_max.append(max([row[j] for row in data]))

    for i in range(n):
        for j in range(m):
            if data[i][j] < row_max[i] and data[i][j] < col_max[j]:
                return 'NO'
    return 'YES'

def solve_all(input_file):
    count = int(input_file.readline().strip())
    for count in range(1, count + 1):
        n, m = [int(s) for s in input_file.readline().strip().split()]
        data = []
        for i in range(n):
            data.append([int(s) for s in input_file.readline().strip().split()])
        print 'Case #{}: {}'.format(count, solve(data, n, m))

solve_all(open(sys.argv[1]))
