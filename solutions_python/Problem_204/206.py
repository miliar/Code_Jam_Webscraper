import logging
from logging import debug as d
from itertools import combinations, permutations
import copy
import math

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


                outfile.write("Case #%d: %s\n" % (i + 1, str(result)))


###=================================== =END TEMPLATE
# logging: d(p(varname=var, varname=var))


def parseTestCase(file):
    line = [int(x) for x in file.readline().strip().split()]
    n = line[0]
    p = [0]

    # n is len(needed)
    needed = [int(x) for x in file.readline().strip().split()]

    have = []
    for i in range(n):
        have.append([int(x) for x in file.readline().strip().split()])

    return needed, have


import networkx as nx
from networkx.algorithms import bipartite

def overlap(a, b):
    amin, amax = a
    bmin, bmax = b

    if amin == bmin:
        return True

    if amin < bmin:
        if amax >= bmin:
            return True

    if bmin < amin:
        if bmax >= amin:
            return True
    return False


def solver(needed, have):
    havecounts = []
    for need, packagesizes in zip(needed, have):
        packagecounts = []
        for i in packagesizes:
            count_ceiling = float(i) / 0.9 / need
            count_floor = float(i) / 1.1 / need
            maxcount = math.floor(count_ceiling)
            mincount = math.ceil(count_floor)

            if maxcount >= mincount:
                packagecounts.append((mincount, maxcount))
        havecounts.append(packagecounts)

    print(needed)
    print(have)
    print(havecounts)

    if len(needed) == 1:
        return len(havecounts[0])

    return find_groups(havecounts)

def find_groups(havecounts):
    first = [(1, x) for x in range(len(havecounts[0]))]
    second = [(2, x) for x in range(len(havecounts[1]))]

    graph = nx.Graph()
    graph.add_nodes_from(first, bipartite=0)
    graph.add_nodes_from(second, bipartite=1)

    for i, tu in enumerate(havecounts[0]):
        for j, ju in enumerate(havecounts[1]):
            if overlap(tu, ju):
                graph.add_edge((1, i), (2, j))

    matching = nx.bipartite.maximum_matching(graph)

    return len(matching) // 2

FILENAME = r"C:\Users\Yaksha\Downloads\B-small-attempt0.in"
#FILENAME = r"K:\downloads\A-small-input.in"
doSolve(FILENAME, solver, True)
