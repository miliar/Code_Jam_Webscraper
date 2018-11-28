#!/usr/bin/env python3

import itertools
import sys
import queue

MINE=-2
GRID=-1

def is_mine(c):
    return 1 if c == MINE else 0

def calc_cell(field, row, col):
    max_row = len(field)
    max_col = len(field[0])

    if field[row][col] == MINE: return MINE

    n = 0
    n += (0 if col == 0         or row == 0         else is_mine(field[row-1][col-1]))
    n += (0 if                     row == 0         else is_mine(field[row-1][col]))
    n += (0 if col == max_col-1 or row == 0         else is_mine(field[row-1][col+1]))
    n += (0 if col == 0                             else is_mine(field[row][col-1]))
    n += (0 if col == max_col-1                     else is_mine(field[row][col+1]))
    n += (0 if col == 0         or row == max_row-1 else is_mine(field[row+1][col-1]))
    n += (0 if                     row == max_row-1 else is_mine(field[row+1][col]))
    n += (0 if col == max_col-1 or row == max_row-1 else is_mine(field[row+1][col+1]))
    return n

def reveal_cell(field, r,c):
    max_row = len(field)
    max_col = len(field[0])

    v = field[r][c]
    if v == MINE: return -1
    if v == GRID:
        n = calc_cell(field, r, c)
        if n >= 0:
            field[r][c] = n
            return n

    return -1

def make_field(stuff, c):
    ret = []
    while len(stuff) > 0:
        ret.append(stuff[0:c])
        stuff = stuff[c:]

    return ret

def solve_field(field, rows, cols, mines):
    q = queue.Queue()
    for sr in range(rows):
        for sc in range(cols):
            if 0 == calc_cell(field, sr, sc):
                break
        else:
            continue
        break
    else:
        return None

    q.put((sr, sc))
    comsume = 0
    while not q.empty():
        (r, c) = q.get()
        if r < 0 or r >= rows or c < 0 or c >= cols: continue
        n = reveal_cell(field, r, c)
        if n >= 0: comsume += 1
        if n==0:
            q.put((r-1,c-1))
            q.put((r-1,c))
            q.put((r-1,c+1))
            q.put((r,c-1))
            q.put((r,c+1))
            q.put((r+1,c-1))
            q.put((r+1,c))
            q.put((r+1,c+1))

    if comsume == (rows*cols - mines):
        return (sr,sc)

    return None

def solve(i,r,c,m):

    print("Case #%d:" % (i+1))
    if r * c - 1 == m:
        field = make_field('c' + '*' * m, c)
        for line in field:
            print(''.join(line))
        return

    for comb in itertools.combinations(range(r*c), m):
        stuff = [GRID] * (r*c)
        for n in comb:
            stuff[n] = MINE
        field = make_field(stuff, c)
        start = solve_field(field, r, c, m)
        if start:
            (sr, sc) = start
            for_print = list('.' * (r*c))
            for n in comb:
                for_print[n] = '*'
            for_print[sr * c +sc] = 'c'
            for line in make_field(for_print, c):
                print(''.join(line))
            break
    else:
        print("Impossible")
            
def main():

    lines = sys.stdin.readlines()
    case_num = int(lines.pop(0))

    for i in range(case_num):
        r,c,m = [int(n) for n in lines.pop(0)[:-1].split(' ')]
        solve(i,r,c,m)

if __name__ == '__main__':
    main()
