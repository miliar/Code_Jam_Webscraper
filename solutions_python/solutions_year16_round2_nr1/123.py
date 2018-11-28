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
    SEQUENCE = [
        ('Z', '0', 'ZERO'),
        ('X', '6', 'SIX'),
        ('G', '8', 'EIGHT'),
        ('U', '4', 'FOUR'),
        ('W', '2', 'TWO'),
        ('R', '3', 'THREE'),
        ('F', '5', 'FIVE'),
        ('S', '7', 'SEVEN'),
        ('O', '1', 'ONE'),
        ('I', '9', 'NINE')
    ]
    def precalculate(self):
        ## User code here
        pass

    def process(self, infile, ncase):
        ## User code here
        string = infile.readline().strip()
        from collections import Counter
        char_count = Counter(string)
        digits = []
        for char, digit, word in self.SEQUENCE:
            count = char_count[char]
            digits += [digit] * count
            for char in word:
                char_count[char] -= count
        assert max(char_count.values()) == 0
        return ''.join(sorted(digits))

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
