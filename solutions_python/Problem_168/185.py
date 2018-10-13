# Round 2 2015
# Problem A. Pegman
# mjacquem1

import sys
import logging
import StringIO
from itertools import chain
import numpy as np

def echo(fn):
    def wrapped(*v, **k):
        name = fn.__name__
        logging.info( "Called %s(%s)" % (name, ", ".join(map(repr, chain(v, k.values())))) )
        res = fn(*v, **k)
        logging.info( "       %s(%s) returned %s" % (name, ", ".join(map(repr, chain(v, k.values()))),res) )
        return res
    return wrapped

direct = {'.':0, '<':1, '^':2, '>':3, 'v':4}

def read_grid(r, c):
    grid = np.zeros((r,c), dtype=int)
    for row in xrange(r):
        line = raw_input()
        for col, char in enumerate(line):
            grid[row, col] = direct[char]
    return grid

increm = { 1: (0,-1), 2: (-1, 0), 3: (0, 1), 4: (1, 0) }
def points_out(grid, row, col, r, c, gdir=0):
    if gdir==0:
        gdir = grid[row, col]
    incrow, inccol = increm[gdir]
    row += incrow
    col += inccol
    while row>=0 and row<r and col>=0 and col<c:
        if grid[row,col] != 0:
            return False
        row += incrow
        col += inccol
    return True

def all_point_out(grid, row, col, r, c):
    return points_out(grid, row, col, r, c, 1) and points_out(grid, row, col, r, c, 2) and points_out(grid, row, col, r, c, 3) and points_out(grid, row, col, r, c, 4)

def solve(grid, r, c):
    res = 0
    for row in xrange(r):
        for col in xrange(c):
            if grid[row,col] != 0:
                if points_out(grid, row, col, r, c):
                    if all_point_out(grid, row, col, r, c):
                        return "IMPOSSIBLE"
                    res += 1
    return res
    
def main(data=None):
    if data is not None:
        sys.stdin = StringIO.StringIO(data)
    for tc in xrange(1, int(raw_input()) + 1):
        r, c = map(int, raw_input().split(' '))
        grid = read_grid(r, c)
        print 'Case #%d: %s' % (tc, solve(grid, r, c))
    if data is not None:
        sys.stdin = sys.__stdin__

sample="""4
2 1
^
^
2 2
>v
^<
3 3
...
.^.
...
1 1
.
"""

# Call main() only if run from command line, not from IDLE
if __name__ == "__main__":
    if True:
#    if '/' not in sys.argv[0] and '\\' not in sys.argv[0]:
        logging.basicConfig(level=logging.ERROR)
        sys.exit(main())
    else:
        logging.basicConfig(level=logging.INFO,format=" %(levelname)s: %(message)s")
