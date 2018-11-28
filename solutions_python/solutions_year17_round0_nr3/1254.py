from collections import defaultdict
import logging
from functools import cmp_to_key
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
    parts = file.readline().strip().split()
    return int(parts[0]), int(parts[1])


def solver(k, n):
    groups = defaultdict(int)
    groups[k] = 1

    num_to_fill = 1
    while n > num_to_fill:
        n -= num_to_fill

        calc_next_group(groups)

        biggest_group = max(groups.keys())
        num_to_fill = groups[biggest_group]

    biggest_group = max(groups.keys())
    new_size = biggest_group - 1

    if new_size == 0:
        return "0 0"
    elif new_size == 1:
        return "1 0"
    else:
        s1 = new_size // 2
        s2 = new_size - s1
        return "%s %s" % (s2, s1)





def calc_next_group(groups):
    biggest_group = max(groups.keys())
    num_groups = groups[biggest_group]

    del groups[biggest_group]

    # there are num_people groups of biggest_group in size
    new_size = biggest_group - 1
    if new_size == 0:
        pass

    elif new_size == 1:
        groups[1] += num_groups

    else:
        s1 = new_size // 2
        s2 = new_size - s1
        groups[s1] += num_groups
        groups[s2] += num_groups

#FILENAME = r"..\test.in"
FILENAME = "K:\Downloads\C-large.in"
doSolve(FILENAME, solver, True)
