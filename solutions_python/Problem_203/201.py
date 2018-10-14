#!/usr/bin/env python3

def solve(rows, cols, grid):
    for r in range(rows):
        for c in range(cols):
            initial = grid[r][c]
            if initial != '?':
                d = r
                while d+1 < rows and grid[d+1][c] == '?':
                    grid[d+1][c] = initial
                    d += 1

    for r in range(rows-1, -1, -1):
        for c in range(cols):
            initial = grid[r][c]
            if initial != '?':
                d = r
                while d-1 >= 0 and grid[d-1][c] == '?':
                    grid[d-1][c] = initial
                    d -= 1

    for r in range(rows-1, -1, -1):
        for c in range(cols-1, -1, -1):
            initial = grid[r][c]
            if initial != '?':
                d = c
                while d-1 >= 0 and grid[r][d-1] == '?':
                    grid[r][d-1] = initial
                    d -= 1

    for r in range(rows):
        for c in range(cols-1, -1, -1):
            initial = grid[r][c]
            if initial != '?':
                d = c
                while d+1 < cols and grid[r][d+1] == '?':
                    grid[r][d+1] = initial
                    d += 1

    return grid

T = int(input())
for i in range(T):
    r, c = [int(n) for n in input().split()]
    grid = []
    for _ in range(r):
        grid.append(list(input()))
    result = [''.join(x) for x in solve(r, c, grid)]
    output = ''.join('\n'.join(result))
    print(f'Case #{i+1}:\n{output}')
