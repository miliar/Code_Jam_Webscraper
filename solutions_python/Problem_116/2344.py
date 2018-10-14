#!/usr/bin/env python3

import sys

def read_matrices():
    with open(sys.argv[1]) as input_file:
        n = int(input_file.readline().strip())
        matrices, matrix = [], []
        for l in input_file.readlines():
            if l.strip():
                matrix.append(list(l.strip()))
            else:
                matrices.append(matrix)
                matrix = []

    return n, matrices

def string_of_result(r):
    if r == 'X':
        return 'X won'
    elif r == 'O':
        return 'O won'
    elif r == 'draw':
        return 'Draw'
    elif r == 'continue':
        return 'Game has not completed'
    else:
        return 'Unknown result: {}'.format(r)

def get_player(m):
    return m[0] if m[0] != 'T' else m[1]

def get_column(m, j):
    c = []
    for i in range(4):
        c.append(m[i][j])
    return c

def get_diagonals(m):
    d1, d2 = [], []
    for i in range(4):
        d1.append(m[i][i])
        d2.append(m[3-i][i])

    return d1, d2

def solve_naive(m):
    # lines
    for i in range(4):
        if all(x == 'O' or x == 'T' for x in m[i]): return 'O'
        elif all(x == 'X' or x == 'T' for x in m[i]): return 'X'

    # columns
    for j in range(4):
        c = get_column(m, j)
        if all(x == 'O' or x == 'T' for x in c): return 'O'
        elif all(x == 'X' or x == 'T' for x in c): return 'X'

    # diagonals
    d1, d2 = get_diagonals(m)
    if all(x == 'O' or x == 'T' for x in d1): return 'O'
    elif all(x == 'X' or x == 'T' for x in d1): return 'X'
    elif all(x == 'O' or x == 'T' for x in d2): return 'O'
    elif all(x == 'X' or x == 'T' for x in d2): return 'X'

    if all(x != '.' for x in [item for sublist in m for item in sublist]):
        return 'draw'

    return 'continue'

n, matrices = read_matrices()

#for m in matrices:
#    for l in m:
#        print(l)

#    print()

for i in range(n):
    print("Case #{}: {}".format(i+1, string_of_result(solve_naive(matrices[i]))))
