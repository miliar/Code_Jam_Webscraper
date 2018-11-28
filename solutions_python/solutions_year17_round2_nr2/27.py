#!/usr/bin/python3
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
        N, R, O, Y, G, B, V = readints(infile)
        pairs = {
            'OB': O,
            'GR': G,
            'VY': V,
        }
        allowed_pair = {'B': 'OB', 'R': 'GR', 'Y': 'VY'}
        counts = {
            'B': B - O,
            'R': R - G,
            'Y': Y - V,
        }
        # Special case: pairs *only*
        if sum(counts.values()) == 0:
            # Special case: pairs *only*
            pairs = [(pair, count) for (pair, count) in pairs.items() if count > 0]
            if len(pairs) != 1:
                return "IMPOSSIBLE"
            else:
                pair, count = pairs[0]
                return pair * count
        allowed = 'BRY'
        arrangement = ''
        while sum(counts.values()) > 0:
            # What to add next?
            first = arrangement[0] if len(arrangement) else ''
            next_type = max(allowed, key=lambda t: counts[t] + (0.5 if t == first else 0))
            if counts[next_type] < 1:
                return "IMPOSSIBLE"
            arrangement += next_type
            counts[next_type] -= 1
            # Any pairs?
            if pairs[allowed_pair[next_type]] > 0:
                arrangement += allowed_pair[next_type] * pairs[allowed_pair[next_type]]
                pairs[allowed_pair[next_type]] = 0
            # What can go next?
            allowed = set('BRY') - set(next_type)
        # Safety checks...
        for c1, c2 in zip(arrangement[1:], arrangement[:-1]):
            assert c1 + c2 in ['BR', 'RY', 'YB', 'BY', 'YR', 'RB', 'OB', 'BO', 'RG', 'GR', 'VY', 'YV']
        if max(pairs.values()) > 0:
            return "IMPOSSIBLE"
        assert len(arrangement) == N
        assert arrangement[0] in 'BRY'
        assert arrangement[-1] in 'BRY'
        if arrangement[0] != arrangement[-1]:
            return arrangement
        else:
            return "IMPOSSIBLE"

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
