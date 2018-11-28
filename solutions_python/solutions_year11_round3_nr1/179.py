#!/usr/bin/env python

import sys

def turn_red(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.' or grid[i][j] == '\\' or grid[i][j] == '/':
                continue
            if i + 1 < len(grid) and j + 1 < len(grid[i]) and \
                grid[i + 1][j] == '#' and grid[i + 1][j + 1] == '#' and \
                grid[i][j + 1] == '#':

                grid[i][j] = '/'
                grid[i][j + 1] = "\\"
                grid[i + 1][j] = "\\"
                grid[i + 1][j + 1] = '/'
            else:
                print('Impossible')
                return

    # Print new grid
    for line in grid:
        print(''.join(line))

if __name__ == '__main__':
    ncases = int(sys.stdin.readline())
    for i in range(ncases):
        r, c = [int(x) for x in sys.stdin.readline().split()]
        grid = []
        for j in range(r):
            grid.append([x for x in sys.stdin.readline().strip('\n')])
        print('Case #', i + 1, ':', sep='')
        turn_red(grid)
