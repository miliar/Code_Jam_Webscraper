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
                result = solver(inputs)
                if log:
                    print(inputs)
                    print(result)
                    print(" ")

                outfile.write("Case #%d: %s\n" % (i + 1, str(result)))


###=================================== =END TEMPLATE
# logging: d(p(varname=var, varname=var))


def parseTestCase(file):
    return [int(x) for x in file.readline().strip()]

def solver(diglist):
    first_bad = -1
    for i in list(range(1, len(diglist)))[::-1]:
        if diglist[i-1] > diglist[i]:
            first_bad = i - 1

    if first_bad == -1:
        return int("".join([str(x) for x in diglist]))

    for i in list(range(1, first_bad + 1))[::-1]:
        if diglist[i-1] == diglist[i]:
            first_bad = i - 1

    if diglist[first_bad] == 1:
        num = [9] * (len(diglist) - 1)
        return int("".join([str(x) for x in num]))

    else:
        diglist[first_bad] -= 1
        for i in range(first_bad + 1, len(diglist)):
            diglist[i] = 9
        return int("".join([str(x) for x in diglist]))

FILENAME = r"K:\Downloads\B-small-attempt1.in"
doSolve(FILENAME, solver, True)
