#!/usr/bin/python3

import re

def solve(R, C, grid):
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '?':
                continue
            if c == C - 1:
                continue
            if grid[r][c + 1] != '?':
                continue
            grid[r][c + 1] = grid[r][c]

    for r in range(R):
        for c in reversed(range(C)):
            if grid[r][c] == '?':
                continue
            if c == 0:
                continue
            if grid[r][c - 1] != '?':
                continue
            grid[r][c - 1] = grid[r][c]

    for c in range(C):
        for r in range(R):
            if grid[r][c] == '?':
                continue
            if r == R - 1:
                continue
            if grid[r + 1][c] != '?':
                continue
            grid[r + 1][c] = grid[r][c]

    for c in range(C):
        for r in reversed(range(R)):
            if grid[r][c] == '?':
                continue
            if r == 0:
                continue
            if grid[r - 1][c] != '?':
                continue
            grid[r - 1][c] = grid[r][c]


def main():
    T = int(input())

    for idx in range(T):
        line = input()
        tokens = re.split(' ', line)
        R = int(tokens[0])
        C = int(tokens[1])

        grid = []
        for i in range(R):
            line = input()
            grid.append(list(line))

        solve(R, C, grid)

        print('Case #{}:'.format(idx + 1))
        for row in grid:
            print(''.join(row))

if __name__ == '__main__':
    main()
