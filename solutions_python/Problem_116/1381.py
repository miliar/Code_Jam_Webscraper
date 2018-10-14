#!/usr/bin/env python

import sys

def check_four(s):
    if "." in s:
        return None
    winners = set(s) - set("T")
    if len(winners) != 1:
        return None
    raise ValueError("%s won" % winners.pop())

def check_grid(grid):
    for line in grid:
        check_four(line)
    for j in range(4):
        check_four([grid[i][j] for i in range(4)])
    check_four([grid[k][k] for k in range(4)])
    check_four([grid[k][3 - k] for k in range(4)])

def parse(file):
    file = open(file)
    grid_nb = int(file.readline())

    for i in range(1, grid_nb + 1):
        grid = [
            file.readline().rstrip(),
            file.readline().rstrip(),
            file.readline().rstrip(),
            file.readline().rstrip(),
            ]
        try:
            check_grid(grid)
        except ValueError as e:
            print("Case #%d: %s" % (i, e))
        else:
            if "." in "".join(grid):
                print ("Case #%d: Game has not completed" % i)
            else:
                print("Case #%d: Draw" % i)
        file.readline()

if __name__ == "__main__":
    parse(sys.argv[1])
