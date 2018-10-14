#!/usr/bin/python

from __future__ import division
from gcj import *

# boolean flags, reachable via OPTS.flagname. Space separated in string
FLAGS = ''

DIRS = [(0,1,'>'),
        (1, 0, 'v'),
        (-1, 0, '^'),
        (0, -1, '<')]

def case():
    R, C = ints()
    grid = []
    for i in range(R):
        grid.append(line())

    switch = 0

    for x in range(R):
        for y in range(C):
            if grid[x][y] == '.': continue

            hitrands = 0
            for dx, dy, tok in DIRS:
                xx = x
                yy = y
                while True:
                    xx += dx
                    yy += dy
                    if xx < 0 or yy < 0 or xx >= R or yy >= C:
                        hitrand = True
                        # rand
                        break
                    if grid[xx][yy] != '.':
                        hitrand = False
                        break # safe
                hitrands += hitrand
                if tok == grid[x][y]:
                    myrand = hitrand
            if myrand:
                switch += 1
                if hitrands == 4:
                    return 'IMPOSSIBLE'
    return switch











if __name__ == '__main__':
    main()
