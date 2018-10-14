#! /usr/bin/env python

from sys import stdin


def solve(num_rows, num_cols, lawn):
    rows = lawn
    cols = [[lawn[r][c] for r in xrange(num_rows)] for c in xrange(num_cols)]

    row_max = [max(row) for row in rows]
    col_max = [max(col) for col in cols]

    for i in xrange(num_rows):
        for j in xrange(num_cols):
            a = lawn[i][j]
            if row_max[i] > a and col_max[j] > a:
                return 'NO'

    return 'YES'


if __name__ == '__main__':
    num_cases = int(stdin.readline().strip())

    for case in range(num_cases):
        n, m = [int(x) for x in stdin.readline().strip().split()]
        lawn = [[int(a) for a in stdin.readline().strip().split()] for i in xrange(n)]
        #print '{} {} {}'.format(n, m, lawn)
        out = solve(n, m, lawn)
        print('Case #{}: {}'.format(case+1, out))


