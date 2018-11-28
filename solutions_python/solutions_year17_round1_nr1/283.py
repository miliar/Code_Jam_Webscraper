from itertools import *

def solve(grid, R, C):
    all_question = '?' * C
    for r in range(1, R):
        if ''.join(grid[r]) == all_question:
            grid[r] = grid[r - 1]
    for r in reversed(range(R - 1)):
        if ''.join(grid[r]) == all_question:
            grid[r] = grid[r + 1]
    for r in range(R):
        for c in range(C):
            char = grid[r][c]
            if char != '?':
                for i in range(c):
                    if grid[r][i] == '?':
                        grid[r][i] = char
        for c in reversed(range(C)):
            char = grid[r][c]
            if char != '?':
                for i in range(c + 1, C):
                    if grid[r][i] == '?':
                        grid[r][i] = char

for case in range(int(raw_input())):
    R, C = map(int,raw_input().split())
    grid = [list(raw_input()) for r in range(R)]
    solve(grid, R, C)
    print "Case #%d:" % (case+1,)
    for r in grid:
        print ''.join(r)
    
