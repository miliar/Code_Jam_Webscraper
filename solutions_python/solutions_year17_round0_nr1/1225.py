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




def parseTestCase(file):
    case = file.readline().strip()
    p = case.split()
    return int(p[1]), [x for x in p[0]]


def solver(k, line):
    moves = 0
    if len(line) >= k:
        for i in range(len(line) - k + 1):
            if line[i] == "-":
                for j in range(k):
                    line[i + j] = "-" if line[i + j] == "+" else "+"
                moves += 1

    if "-" in line:
        return "IMPOSSIBLE"
    else:
        return str(moves)

FILENAME = r"K:\Downloads\A-large.in"
doSolve(FILENAME, solver, True)
