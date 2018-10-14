import logging
from logging import debug as d
from itertools import combinations, permutations
import copy

EPS = 10 ** -6

logging.basicConfig(level=logging.DEBUG, format=('%(funcName)s(%(lineno)d):  %(message)s'))

def p(**kwargs):
    printstr = ''
    for (key, var) in kwargs.items():
        printstr += ("%s=%s\t" % (key, var))

    return printstr


def doSolve(filename, solver, log=False):
    with open(filename) as infile:
        with open(filename + ".out", 'w') as outfile:
            numCases = int(infile.readline())

            for i in range(numCases):
                inputs = parseTestCase(infile)
                result = solver(copy.deepcopy(inputs))
                if log:
                    print(inputs)
                    print(result)
                    print(" ")

                outfile.write("Case #%d: %s\n" % (i + 1, str(result)))


###=================================== =END TEMPLATE
# logging: d(p(varname=var, varname=var))


def parseTestCase(file):
    shape = [int(x) for x in file.readline().strip().split()]
    rows = shape[0]
    grid = []
    for i in range(rows):
        grid.append([x for x in file.readline().strip()])
    return grid

def fillrow(row):
    first = find_first(row)
    if first is None:
        return

    filler = first
    for i, letter in enumerate(row):
        if letter == '?':
            row[i] = filler
        else:
            filler = letter

def find_first(row):
    for letter in row:
        if letter != '?':
            return letter
    return None

def first_good_row(grid):
    for row in grid:
        if find_first(row) is not None:
            return row

def solver(grid):
    for row in grid:
        fillrow(row)

    filler_row = first_good_row(grid)
    for i, row in enumerate(grid):
        if find_first(row) is None:
            grid[i] = filler_row
        else:
            filler_row = row

    retstr = "\n" + "\n".join(["".join(x) for x in grid])

    return retstr

FILENAME = r"C:\Users\Yaksha\Downloads\A-large.in"
#FILENAME = r"K:\downloads\A-small-input.in"
doSolve(FILENAME, solver, True)
