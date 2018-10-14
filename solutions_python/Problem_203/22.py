#! /usr/bin/python2.7

def inner_solve(_grid, _outliers, i, j):
    while i < R and _grid[i][j] != "?":
        j += 1
        if j == C:
            j = 0
            i += 1
    if i == R:
        return _grid
    for k in _outliers.keys():
        grid = [r[:] for r in _grid]
        outliers = dict(_outliers)
        ib, ie, jb, je = outliers[k]
        ib, ie, jb, je = min(ib, i), max(ie, i + 1), min(jb, j), max(je, j + 1)
        outliers[k] = ib, ie, jb, je
        not_it = False
        for _i in xrange(ib, ie):
            for _j in xrange(jb, je):
                if grid[_i][_j] not in ["?", k]:
                    not_it = True
                    break
                grid[_i][_j] = k
            if not_it:
                break
        if not_it:
            continue
        rv = inner_solve(grid, outliers, i , j)
        if rv is not None:
            return rv
    return None
        
    
def solve(grid):
    outliers = {}
    for i in xrange(R):
        for j in xrange(C):
            if grid[i][j] != "?":
                outliers[grid[i][j]] = (i, i + 1, j, j + 1)
    return inner_solve(grid, outliers, 0, 0)
    
import sys
f = sys.stdin
#f = open("q1_example.in")
T = int(f.readline())
for i in xrange(1, T + 1):
    R, C = map(int, f.readline().split())
    grid = []
    for j in xrange(R):
        grid.append(map(lambda x: x, f.readline().strip()))
    print "Case #%d:" % (i)
    print "\n".join("".join(r) for r in solve(grid))