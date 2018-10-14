#!/usr/bin/python2
### Google Code Jam template
# Futures
from __future__ import division
from __future__ import with_statement
from __future__ import print_function


## Library
# @memoized
def memoized(func):
    mem = {}

    def wrapped(*args):
        if args not in mem:
            mem[args] = func(*args)
        return mem[args]
    return wrapped

## Input templates
# Line as int
readint = lambda infile: int(infile.readline())
# Line as many ints
readints = lambda infile: [int(s) for s in infile.readline().split()]


# Base class
class ProblemSolver(object):
    def __init__(self):
        self.precalculate()

    def precalculate(self):
        raise NotImplementedError

    def process(self, infile, ncase):
        raise NotImplementedError

    def run(self, infile, outfile):
        cases = int(infile.readline())
        for ncase in range(cases):
            print("Case #{nc}".format(nc=ncase + 1))
            # Perform all nessesary calculation
            data = self.process(infile, ncase=ncase)
            outfile.write("Case #{nc}: {data}\n".format(
                nc=ncase + 1, data=data))


# Working class
class Solver(ProblemSolver):
    def precalculate(self):
        ## User code here
        pass

    def process(self, infile, ncase):
        ## User code here
        ingr_count, pack_count = readints(infile)
        ingr_needed = readints(infile)
        ingr_amounts = [sorted(readints(infile)) for i in range(ingr_count)]
        ingr_servings = [
            [(10 * amount // (9 * needed), (10 * amount - 1) // (11 * needed) + 1) for amount in amounts]
            for (needed, amounts) in zip(ingr_needed, ingr_amounts)]
        total_kits = 0
        #print(ingr_servings)
        while min([len(ingr) for ingr in ingr_servings]):
            # Max one ingridient allows us to
            servings_limit = min([ingr[-1][0] for ingr in ingr_servings])
            if max([ingr[-1][1] for ingr in ingr_servings]) <= servings_limit:
                # Ok, we can serve it from the biggest packages everywhere
                total_kits += 1
                for ingr in ingr_servings:
                    ingr.pop()
            else:
                # Sorry, some of the biggest packages are just too big
                for ingr in ingr_servings:
                    while ingr and ingr[-1][1] > servings_limit:
                        ingr.pop()
        return total_kits

# Script code
if __name__ == '__main__':
    ## Setup
    # Task letter
    from os.path import basename, splitext
    TASK = splitext(basename(__file__))[0]
    print("Task {}".format(TASK))
    from sys import argv
    if len(argv) > 1:
        print("Filename given: {}".format(argv[1]))
        FILE = splitext(argv[1])[0]
    else:
        FILE = TASK
    ## Precalculation
    print("Initialization...")
    solver = Solver()
    print("Initialization done.")
    ## Calculation
    print("Calculation...")
    with open(FILE + ".in") as infile:
        with open(FILE + ".out", mode="wt") as outfile:
            solver.run(infile, outfile)
    print("Calculation done.")
