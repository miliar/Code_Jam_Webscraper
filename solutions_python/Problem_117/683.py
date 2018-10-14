#!/usr/bin/env python

import sys
import IPython

debug = 0

def print_matrix(matrix):
    print '------------------'
    for line in matrix:
        print line

def get_col(m, n, matrix, j):
    col = []
    for i in xrange(m+2):
        col.append(matrix[i][j])
    return col


def handle_matrix(m, n, matrix):
    #print m, n
    #print '---------'
    #print matrix
    #print '---------'

    for i in xrange(m+2):
        for j in xrange(n+2):

            c = matrix[i][j]

            if c == 0:
                continue

            hor = (c < max(matrix[i][:]))

            col = get_col(m, n, matrix, j)

            ver = (c < max(col[:]))

            if debug: print '(%s,%s)=%s. %s - %s' % (
                i,j,c,hor,ver)

            if hor and ver:
                return False

    return True

lines = open(sys.argv[1]).read().split('\n')

test_num=int(lines[0])

idx=1
for x in xrange(test_num):
    curr_line = lines[idx]
    idx += 1

    m, n = map(int, curr_line.split(' '))

    matrix = []
    matrix.append([0] * (n+2))
    for _ in xrange(m):
        curr_line = lines[idx]
        idx += 1

        row = map(int, curr_line.split(' '))
        row = [0] + row + [0]
        matrix.append(row)
    matrix.append([0] * (n+2))

    ispossible = handle_matrix(m, n, matrix)
    if debug: print_matrix(matrix)
    print 'Case #%s: %s' % (x+1, 'YES' if ispossible else 'NO')
    if debug: IPython.embed()
