#!/usr/bin/python3

import sys

n = int(sys.stdin.readline())

puscice = ['^', 'v', '<', '>']

def all_free(grid, r, c, r0, c0):
    for i in range(r):
        if i == r0:
            continue
        if grid[i][c0] != '.':
            return False
    for i in range(c):
        if i == c0:
            continue
        if grid[r0][i] != '.':
            return False
    return True

def solve(r, c, grid):
    bad_guys = 0
    can_fix = True
    # z leve
    for i in range(r):
        for j in range(c):
            if grid[i][j] in puscice:
                if grid[i][j] == '<':
                    bad_guys += 1
                    if all_free(grid, r, c, i, j):
                        can_fix = False
                break
    for i in range(r):
        for j in range(c-1, -1, -1):
            if grid[i][j] in puscice:
                if grid[i][j] == '>':
                    bad_guys += 1
                    if all_free(grid, r, c, i, j):
                        can_fix = False
                break
    for j in range(c):
        for i in range(r):
            if grid[i][j] in puscice:
                if grid[i][j] == '^':
                    bad_guys += 1
                    if all_free(grid, r, c, i, j):
                        can_fix = False
                break
    for j in range(c):
        for i in range(r-1, -1, -1):
            if grid[i][j] in puscice:
                if grid[i][j] == 'v':
                    bad_guys += 1
                    if all_free(grid, r, c, i, j):
                        can_fix = False
                break            
    if not can_fix:
        return None
    return bad_guys

for case_num in range(1, n+1):
    r, c = map(int, sys.stdin.readline().split())
    grid = [list(sys.stdin.readline().strip()) for i in range(r)]
    sol = solve(r, c, grid)
    if sol is None:
        print('Case #{0}: IMPOSSIBLE'.format(case_num))
    else:
        print('Case #{0}: {1}'.format(case_num, sol))
        