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
                result = solver(*inputs)
                if log:
                    print(inputs)
                    print(result)
                    print(" ")

                outfile.write("Case #%d: %s\n" % (i + 1, str(result)))


###=================================== =END TEMPLATE
# logging: d(p(varname=var, varname=var))


def parseTestCase(file):
    ac, aj = [int(x) for x in file.readline().strip().split()]
    aclist = []
    for i in range(ac):
        [start, stop] = [int(x) for x in file.readline().strip().split()]
        aclist.append((start, stop))

    ajlist = []
    for i in range(aj):
        [start, stop] = [int(x) for x in file.readline().strip().split()]
        ajlist.append((start, stop))

    return aclist, ajlist

def solver(aclist, ajlist):
    if len(aclist) == 2:
        nel = aclist
    elif len(ajlist) == 2:
        nel = ajlist
    else:
        return "2"

    # see if the two activities can be grouped in a single 720min group
    nel.sort()
    if (nel[1][1] - nel[0][0]) <= 720:
        return "2"
    elif ((nel[0][1] + 1440) - nel[1][0]) <= 720:
        return "2"
    else:
        return "4"


def span(interval1, interval2):
    larger = interval1[1]
    smaller = interval2[0]

    if larger < smaller:
        larger += 1440

    return larger - smaller


FILENAME = r"K:\Downloads\B-small-attempt0.in"
#FILENAME = r"K:\downloads\A-small-input.in"
doSolve(FILENAME, solver, True)
