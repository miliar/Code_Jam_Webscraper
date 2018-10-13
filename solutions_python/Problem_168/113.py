
import os
import sys
import glob
import subprocess
import random
import fileinput
import operator


next_line = 0
lines = [line.strip() for line in fileinput.input()]


def get_line():
    global next_line
    i = next_line
    next_line += 1
    return lines[i]


up = '^'
down = 'v'
left = '<'
right = '>'


def ok(grid, r, c):
    R = len(grid)
    C = len(grid[0])

    visited = [[False for i in range(C)] for j in range(R)]
    points = [(r, c, grid[r][c])]
    n = 0
    visited[r][c] = True
    while n < len(points):
        r, c, d = points[n][0], points[n][1], points[n][2]
        nr, nc, nd = r, c, d
        if d == up:
            nr -= 1
        elif d == down:
            nr += 1;
        elif d == left:
            nc -= 1
        else:
            nc += 1
        if nr < 0 or nr >= R or nc < 0 or nc >= C:
            return False
        # print nr, nc, R, C, len(visited), len(visited[0])
        if visited[nr][nc]:
            return True
        if grid[nr][nc] != '.':
            return True
        points.append((nr, nc, nd))
        visited[nr][nc] = True
        n += 1
    return True


def calc():
    R, C = map(int, get_line().split())
    grid = [[ch for ch in get_line()] for i in range(R)]

    """
    for r in range(R):
        for c in range(C):
            print grid[r][c],
        print
    print
    """

    visited = [[False for i in range(C)] for j in range(R)]
    ans = 0
    """
    for r in range(R):
        for c in range(C):
            ch = grid[r][c]
            if r == 0 and c == 0:
                if ch == up or ch == left:
                    ans += 1
                    grid[r][c] = down
                    visited[r][c] = True
            elif r == 0 and c == C-1:
                if ch == up or ch == right:
                    ans += 1
                    grid[r][c] = down
                    visited[r][c] = True
            elif r == R-1 and c == 0:
                if ch == down or ch == left:
                    ans += 1
                    grid[r][c] = up
                    visited[r][c] = True
            elif r == R-1 and c == C-1:
                if ch == down or ch == right:
                    ans += 1
                    grid[r][c] = up
                    visited[r][c] = True
            elif r == 0:
                if ch == up:
                    ans += 1
                    grid[r][c] = down
                    visited[r][c] = True
            elif r == C-1:
                if ch == down:
                    ans += 1
                    grid[r][c] = up
                    visited[r][c] = True
            elif c == 0:
                if ch == left:
                    ans += 1
                    grid[r][c] = right
                    visited[r][c] = True
            elif c == C-1:
                if ch == right:
                    ans += 1
                    grid[r][c] = left
                    visited[r][c] = True
    """

    for r in range(0, R):
        for c in range(0, C):
            if grid[r][c] == '.':
                continue
            if visited[r][c]:
                continue
            # print r, c
            if ok(grid, r, c):
                continue
            old = grid[r][c]
            good = False
            for nn in (up, down, left, right):
                if nn != old:
                    grid[r][c] = nn
                    if ok(grid, r, c):
                        good = True
                        break
            if not good:
                return 'IMPOSSIBLE'
            ans += 1


    return ans

T = int(get_line())
for i in range(1, T + 1):
    print('Case #%d: %s' % (i, calc()))
