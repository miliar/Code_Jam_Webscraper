# Google Code Jam 2009
# Qualification Round - "Watersheds"
# Author: Richard Ledley
# Python 2.5


def trace(grid, solution, row, col, label):
    """
    Fills in 'solution' with the number of the basin
    the supplied row/col drains into. Also labels any
    intermediate cells, including the basin itself.

    'label' is the next unused basin number

    returns a tuple (label of supplied cell, next available label)
    """

    # Hits a stream with which supplied cell converges
    if solution[row][col] is not None:
        return solution[row][col], label

    to_row, to_col = drains_to(grid, row, col)
    if to_row is None: # if it's a sink
        solution[row][col] = label
        return (label, label+1)
    ans, next_avail = trace(grid, solution, to_row, to_col, label)
    solution[row][col] = ans
    return (ans, next_avail)


def is_sink(grid, row, col):
    """
    Returns boolean whether or not supplied row, col is a sink
    """
    return drains_to(grid, row, col) is None

def drains_to(grid, row, col):
    """
    Returns coordinates ot the cell cupplied row,col drains into immediately

    Returns (None, None) if supplied row, col is a sink
    """
    if row == 0:
        north = None
    else:
        north = grid[row-1][col]
    if row == len(grid)-1:
        south = None
    else:
        south = grid[row+1][col]
    if col == 0:
        west = None
    else:
        west = grid[row][col-1]
    if col == len(grid[0])-1:
        east = None
    else:
        east = grid[row][col+1]

    if north is None and south is None and east is None and west is None:
        return (None, None) # Hack in the 4-minute submission time
    to_depth = min([val for val in [north, west, east, south] if val is not None])
    if to_depth >= grid[row][col]:
        return (None, None)
    if north == to_depth:
        return (row-1, col)
    elif west == to_depth:
        return (row, col-1)
    elif east == to_depth:
        return (row, col+1)
    elif south == to_depth:
        return (row+1, col)
    else:
        raise "Error in draining cell %s,%s" % (row, col)
    

def solve(grid, solution):
    """
    Solves a complete grid
    """
    current_label = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            sol, new_lbl = trace(grid, solution, row, col, current_label)
            current_label = new_lbl



import string
from string import ascii_lowercase as labels
print "File?"
file = open(raw_input())
num_maps =  int(file.readline())

for x in range(num_maps):
    print "Case #%s:" % (x+1)
    height, width  = [int(num) for num in file.readline().split()]
    grid = []
    solution = []
    for y in range(height):
        row = [int(num) for num in file.readline().split()]
        grid.append(row)
        solution.append([None for x in range(len(row))])
    solve(grid, solution)
    for row in solution:
        print " ".join([labels[x] for x in row])

