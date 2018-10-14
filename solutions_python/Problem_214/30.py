#!/usr/bin/env python3

# Google Code Jam Round 2 2017
# Problem C. Beaming With Joy
# Solution in Python 3
# By Smithers

def solve(r, c, grid):
    for i in range(r):
        for j in range(c):
            if grid[i][j] not in '-|':
                continue
            canv = True
            for i2 in reversed(range(i)):
                if grid[i2][j] in '+-|':
                    canv = False
                if grid[i2][j] in '+-|#':
                    break
            for i2 in range(i + 1, r):
                if grid[i2][j] in '+-|':
                    canv = False
                if grid[i2][j] in '+-|#':
                    break
            canh = True
            for j2 in reversed(range(j)):
                if grid[i][j2] in '+-|':
                    canh = False
                if grid[i][j2] in '+-|#':
                    break
            for j2 in range(j + 1, c):
                if grid[i][j2] in '+-|':
                    canh = False
                if grid[i][j2] in '+-|#':
                    break
            if not canv and not canh:
                return False
            elif not canv:
                grid[i][j] = '-'
            elif not canh:
                grid[i][j] = '|'
            else:
                grid[i][j] = '+'
    
    change = True
    while change:
        change = False
        for i in range(r):
            for j in range(c):
                if grid[i][j] != '.':
                    continue
                canv = False
                for i2 in reversed(range(i)):
                    if grid[i2][j] in '+|':
                        canv = True
                    if grid[i2][j] in '+-|#':
                        break
                for i2 in range(i + 1, r):
                    if grid[i2][j] in '+|':
                        canv = True
                    if grid[i2][j] in '+-|#':
                        break
                if not canv:
                    canh = False
                    for j2 in reversed(range(j)):
                        if grid[i][j2] in '+-':
                            canh = True
                            change = change or grid[i][j2] == '+'
                            grid[i][j2] = '-'
                        if grid[i][j2] in '+-|#':
                            break
                    for j2 in range(j + 1, c):
                        if grid[i][j2] in '+-':
                            canh = True
                            change = change or grid[i][j2] == '+'
                            grid[i][j2] = '-'
                        if grid[i][j2] in '+-|#':
                            break
                    if not canh:
                        return False
    
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '+':
                grid[i][j] = '|'
    
    return True

for x in range(1, int(input()) + 1):
    r, c = map(int, input().split())
    grid = [list(input()) for i in range(r)]
    
    if solve(r, c, grid):
        print('Case #{}: POSSIBLE'.format(x))
        for row in grid:
            print(*row, sep='')
    else:
        print('Case #{}: IMPOSSIBLE'.format(x))
