import numpy as np

def check_right(grid, x, y) :
    R, C = grid.shape
    if x == C-1: return False
    for ix in range(x+1, C) :
        if grid[y][ix] != '.':
            return True
    return False

def check_left(grid, x, y) :
    if x == 0: return False
    for ix in range(x) :
        if grid[y][ix] != '.':
            return True
    return False

def check_top(grid, x, y) :
    if y == 0: return False
    for iy in range(y) :
        if grid[iy][x] != '.':
            return True
    return False

def check_down(grid, x, y) :
    R, C = grid.shape
    if y == R-1: return False
    for iy in range(y+1, R) :
        if grid[iy][x] != '.':
            return True
    return False

def check(grid, x, y):
    if grid[y][x] == '>': return check_right(grid, x, y)
    if grid[y][x] == '<': return check_left(grid, x, y)
    if grid[y][x] == '^': return check_top(grid, x, y)
    if grid[y][x] == 'v': return check_down(grid, x, y)
    return False

def change(grid, x, y) :
    if check_right(grid, x, y):
        grid[y][x] = '>'
        return True
    if check_left(grid, x, y):
        grid[y][x] = '<'
        return True
    if check_top(grid, x, y):
        grid[y][x] = '^'
        return True
    if check_down(grid, x, y):
        grid[y][x] = 'v'
        return True
    return False

def solveA(grid) :
    R, C = grid.shape
    changes = 0
    for y in range(R):
        for x in range(C):
            if grid[y][x] != '.':
                if not check(grid, x, y):
                    if not change(grid, x, y) :
                        return -1
                    else :
                        changes += 1
    return changes

def solve(in_filename, out_filename):
    with open(in_filename, 'r') as file, open(out_filename, 'w') as ofile :
        T = int(file.next())
        for case in range(0, T) :
            line = file.next()
            tok = line.split()
            R = int(tok[0])
            C = int(tok[1])
            grid = np.empty((R, C), dtype='|S1')
            for y in range(R):
                line = file.next()
                for x in range(C):
                    grid[y, x] = line[x]


            sol = solveA(grid)
            if sol == -1 :
                ofile.write("Case #%d: IMPOSSIBLE\n"%(case+1))
            else:
                ofile.write("Case #%d: %d\n"%(case+1, sol))

if __name__ == '__main__':
    import sys
    import os
    _, input = sys.argv
    output = os.path.splitext(input)[0] + '.out'
    solve(input, output)
