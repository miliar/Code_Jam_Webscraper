import math
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

    (k, n) = [int(x) for x in file.readline().strip().split()]
    pancakes = []
    for i in range(k):
        (r, h) = [int(x) for x in file.readline().strip().split()]
        pancakes.append((r, h))

    return n, pancakes

def solver(n, pancakes):
    pancakes = [(r, h, calc_outside_area(r, h)) for (r, h) in pancakes]
    pancakes = sorted(pancakes)
    pancakes = pancakes[::-1]

    best = 0
    best_h = 0
    best_r = 0
    cur_radius = None
    print(str(n) + "  " + str(pancakes))
    for (i, cake) in enumerate(pancakes):
        (r, h, sa) = cake
        if cur_radius is None:
            cur_radius = r
            best = calculate(pancakes[:i] + pancakes[i+1:], r, h, sa, n-1)
            best_h = h
            best_r = r
        elif r != cur_radius:
            cur_radius = r
            if calc_all_area(r, h) >= calc_all_area(best_r, best_h):
                best = max(best, calculate(pancakes[:i] + pancakes[i+1:], r, h, sa, n-1))

    return best

def calculate(pancakes, r, h, sa, n):

    pancake_pool = [x for x in pancakes if x[0] <= r]
    if len(pancake_pool) < n:
        return 0

    pancake_pool.sort(key=lambda x: x[2])
    pancake_pool = pancake_pool[::-1]
    pancake_pool = pancake_pool[:n]
    print(pancake_pool)
    return calc_top_area(r, h) + sa + sum(x[2] for x in pancake_pool)


def calc_top_area(r, h):
    return math.pi * r * r

def calc_all_area(r, h):
    return calc_top_area(r, h) + calc_outside_area(r, h)


def calc_outside_area(r, h):
    return math.pi * 2 * r * h

#FILENAME = r"..\test.in"
FILENAME = "K:\Downloads\A-large.in"
doSolve(FILENAME, solver, True)
