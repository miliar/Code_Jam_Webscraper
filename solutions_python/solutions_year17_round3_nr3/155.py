from operator import mul
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
    (n, k) = [int(i) for i in file.readline().strip().split()]
    u = float(file.readline().strip())
    cores = [float(i) for i in file.readline().strip().split()]
    return n, k, u, cores

def solver(n, k, u, cores):
    while u > 0:
        cores.sort()
        print(cores)

        lowest, lowest2, numlow = peak(cores)
        if lowest2 is None:
            # all cores at same probability
            lowest += (u / numlow)
            cores = [lowest] * numlow
            break

        else:
            diff = lowest2 - lowest
            if u >= diff * numlow:
                u -= diff * numlow
                cores = [lowest2] * numlow + cores[numlow:]
            else:
                newlow = lowest + u / numlow
                cores = [newlow] * numlow + cores[numlow:]
                break

    return calculate(cores)

def peak(alist):
    lowest = None
    numlowest = 0
    lowest2 = None
    for x in alist:
        if lowest is None:
            lowest = x
            numlowest += 1
        elif x == lowest:
            numlowest += 1
        else:
            lowest2 = x
            break

    return lowest, lowest2, numlowest

def calculate(cores):
    if len(cores) == 1:
        return cores[0]

    val = cores[0]
    for i in cores[1:]:
        val = val * i
    return val


FILENAME = "K:\Downloads\C-small-1-attempt0.in"
#FILENAME = r"K:\downloads\A-small-input.in"
doSolve(FILENAME, solver, True)
