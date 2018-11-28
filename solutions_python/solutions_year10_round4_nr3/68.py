#!/usr/bin/python

from __future__ import print_function

import copy
import itertools
import sys

def main(filename):
    with open(filename, "r") as f:
        for case, line in enumerate(f):
            if not case:
                C = int(line.strip())
                continue
            if case > C:
                break
            R = int(line.strip())
            lines = []
            for i in xrange(R):
                line = next(f)
                lines.append([int(c) for c in line.split()])
            grid = set()
            for line in lines:
                for x in xrange(line[0], line[2]+1):
                    for y in xrange(line[1], line[3]+1):
                        grid.add((x,y))
            value = solve(grid)
            print("Case #{0}: {1}".format(case,value))


def solve(grid):
    for time in itertools.count():
        if grid:
            grid = evolve(grid)
        else:
            return time



def evolve(grid):
    newgrid = set(grid)
    for x,y in grid:
        if ((x-1,y) not in grid) and ((x,y-1) not in grid):
            newgrid.remove((x,y))
        if ((x,y+1) not in grid) and ((x-1,y+1) in grid):
            newgrid.add((x,y+1))
    assert newgrid != grid
    return newgrid


if __name__ == "__main__":
    main(sys.argv[1])
    sys.exit(0)

