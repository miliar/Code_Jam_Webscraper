#!/usr/bin/env python

import numpy

problem = 'C-small-attempt1'

fin = open(problem + '.in')
fout = open(problem + '.out', 'w')

def read_ints():
    return [int(x) for x in fin.readline().strip().split()]

def transpose(grid):
    return zip(*grid)

def wide_grid(grid):
    """Return a view on the grid that's got more columns than rows"""
    R, C = grid.shape
    if R > C:
        return grid.T
    else:
        return grid

def test_grid(grid, M):
    """Fill a sub-grid, assume grid is currently wide"""
    R, C = grid.shape

    if R * C - M == 1:
        grid[:,:] = 1.0
        grid[-1,-1] = 0
        return True

    if R == 2:
        # We can get at least a 2x2 square
        if M % 2 == 0 and M / 2 <= C - 2:
            for i in range(M/2):
                grid[:,i] = 1.0
            return True
        else:
            return False

    if M <= C-2:
        grid[0,0:M] = 1.0
        return True

    if M <= C-2 + R-3:
        grid[0,0:C-2] = 1.0
        grid[1:M-(C-2)+1, 0] = 1.0
        return True

    if M >= C and test_grid(wide_grid(grid[1:,:]), M-C):
        grid[0,:] = 1.0
        return True

    if M >= R and test_grid(wide_grid(grid[:,1:]), M-R):
        grid[:,0] = 1.0
        return True

    return False

T = int(fin.readline())

for caseno in range(T):
    R, C, M = read_ints()

    base_grid = numpy.zeros((R, C))
    grid = wide_grid(base_grid)

    if grid.shape[0] > 1:
        it_worked = test_grid(grid, M)
    else:
        grid[0,0:M] = 1.0
        it_worked = True

    if it_worked:
        fout.write("Case #%d:\n" % (caseno+1))
        base_grid[-1,-1] = -1.0
        to_print = {1.0: '*', 0.0: '.', -1.0: 'c'}
        for row in base_grid:
            fout.write(''.join(to_print[x] for x in row))
            fout.write('\n')
    else:
        fout.write("Case #%d:\nImpossible\n" % (caseno+1))


fout.close()

