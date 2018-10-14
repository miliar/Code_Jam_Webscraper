#!/usr/bin/env python
import sys

def read_line(): return sys.stdin.readline().strip()
def read_int(): return int(sys.stdin.readline())
def read_ints(): return [int(x) for x in sys.stdin.readline().split()]

def solve(rows, cols, table):
    ok_table = [[False] * cols for i in range(rows)]

    # horizontal cut
    for y in range(rows):
        h_max = max(table[y])
        for x in range(cols):
            if table[y][x] == h_max:
                ok_table[y][x] = True

    # vertical cut
    for x in range(cols):
        v_max = 0
        for y in range(rows):
            v_max = max(v_max, table[y][x])
        for y in range(rows):
            if table[y][x] == v_max:
                ok_table[y][x] = True

    # check
    for a in ok_table:
        if False in a:
            return 'NO'

    return 'YES'

if __name__ == '__main__':
    T = read_int()
    for i in range(T):
        N, M = read_ints()
        table = []
        for y in range(N): table.append(read_ints())
        print('Case #{}: {}'.format(i+1, solve(N, M, table)))

