#!/usr/bin/python

import sys

def move(line):
    compress = ''.join([c for c in line if c != '.'])
    n = len(line)
    m = len(compress)
    return ''.join([''.join(['.' for i in xrange(n - m)]), compress])

def count_vert(grid, i):
    s = ''.join([x[i] for x in grid])
    return count_hor(s)

def count_hor(s):
    prev = None
    ct = 1
    stats = {'.': 0, 'R': 0, 'B': 0}
    for c in s:
        if prev == c: ct += 1
        elif prev is not None:
            stats[prev] = max(stats.get(prev, 0), ct)
            ct = 1
        prev = c
    stats[prev] = max(stats.get(prev, 0), ct)
    return stats

def count_diag(grid, n, dim):
    if n <= dim:
        s = ''.join([grid[i][(n - 1) - i] for i in xrange(n)])
    else:
        s = ''.join([grid[i][(n - 1) - i] for i in xrange(n - dim, dim)])
    return count_hor(s)    

def count_diag2(grid, n, dim):
    new_grid = [s[::-1] for s in grid]
    return count_diag(new_grid, n, dim)

def solve(grid, dim, need):
    red_wins = False
    blue_wins = False
    for s in grid:
        hstats = count_hor(s)
        red_wins = red_wins or need <= hstats['R']
        blue_wins = blue_wins or need <= hstats['B']
    for i in xrange(dim):
        vstats = count_vert(grid, i)
        red_wins = red_wins or need <= vstats['R']
        blue_wins = blue_wins or need <= vstats['B']
    for n in xrange(need, 2 * dim):
        diagstats = count_diag(grid, n, dim)
        red_wins = red_wins or need <= diagstats['R']
        blue_wins = blue_wins or need <= diagstats['B']
    for n in xrange(need, 2 * dim):
        diagstats = count_diag2(grid, n, dim)
        red_wins = red_wins or need <= diagstats['R']
        blue_wins = blue_wins or need <= diagstats['B']
    if red_wins and blue_wins: return 'Both'
    if red_wins: return 'Red'
    if blue_wins: return 'Blue'
    else: return 'Neither'

f = open(sys.argv[1])
num_cases = int(f.next())
for casenum in xrange(num_cases):
    dim, need = map(int, f.next().split(' '))
    grid = []
    for i in xrange(dim):
        grid.append(move(f.next().rstrip('\n')))
    print 'Case #%i: %s'%(casenum + 1, solve(grid, dim, need))

