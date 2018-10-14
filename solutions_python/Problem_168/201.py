#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 KuoE0 <kuoe0.tw@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

def get_direction(d):
    if d == '^':
        return (-1, 0)
    if d == 'v':
        return (1, 0)
    if d == '>':
        return (0, 1)
    if d == '<':
        return (0, -1)

def index_check(size, idx):
    return 0 <= idx < size

def try_direction(grid, r, c):
    R, C = len(grid), len(grid[0])
    dir_r, dir_c = get_direction(grid[r][c])
    next_r, next_c = r + dir_r, c + dir_c


def boundary_count(grid):
    import copy
    new_grid = copy.deepcopy(grid)

    if len(grid[0]) > 1:
        for i in range(len(grid)):
            if grid[i][0] == '<':
                new_grid[i][0] = '>'
            if grid[i][-1] == '>':
                new_grid[i][-1] = '<'

    if len(grid) > 1:
        for i in range(len(grid[0])):
            if grid[0][i] == '^':
                new_grid[0][i] = 'v'
            if grid[-1][i] == 'v':
                new_grid[-1][i] = '^'

    cnt = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != new_grid[i][j]:
                cnt = cnt + 1

    return new_grid, cnt

def is_go_outside(grid, r, c, dir = None):
    R, C = len(grid), len(grid[0])
    if not dir:
        dir = grid[r][c]
    dir_r, dir_c = get_direction(dir)
    while True:
        r, c = r + dir_r, c + dir_c
        if index_check(R, r) and index_check(C, c):
            if grid[r][c] != '.':
                return False
        else:
            return True

def is_impossible(grid):

    cnt = 0
    R, C = len(grid), len(grid[0])
    for i in range(R):
        for j in range(C):
            if grid[i][j] != '.' and is_go_outside(grid, i, j):
                for d in ['^', 'v', '<', '>']:
                    if d != grid[i][j] and not is_go_outside(grid, i, j, d):
                        cnt = cnt + 1
                        break
                else:
                    return True, cnt

    return False, cnt

T = int(input())
for t in range(T):
    R, C = [int(x) for x in input().split()]

    grid = []
    for i in range(R):
        grid.append(list(input()))

    grid, cnt1 = boundary_count(grid)
    flag, cnt2 = is_impossible(grid)

    if flag:
        print("Case #{0}: IMPOSSIBLE".format(t + 1))
    else:
        print("Case #{0}: {1}".format(t + 1, cnt1 + cnt2))




