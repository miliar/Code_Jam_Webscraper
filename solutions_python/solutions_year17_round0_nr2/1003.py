# Written by Nikolai Artemiev

import collections
import functools
import itertools
import math
import matplotlib.pyplot
import multiprocessing
import numpy
import os
import resource
import scipy
import sys


def solve(N):
    for i in range(1, len(N)):
        if int(N[i - 1]) > int(N[i]):
            prefix = str(int(N[:i]) - 1)
            suffix = "9" * (len(N) - i)
            return solve(str(int(prefix + suffix)))
    return N



def read(F):
    return [F.readline().strip()]


if __name__ == "__main__":
    # Resize stack to useful size
    recursion_limit = 100000
    resource.setrlimit(resource.RLIMIT_STACK, [resource.RLIM_INFINITY, resource.RLIM_INFINITY])
    sys.setrecursionlimit(recursion_limit)

    input_file = "B-large.in"

    # Read cases
    with open(input_file) as F:
        T = int(F.readline())
        cases = [read(F) for case in range(T)]

    # Solve
    def expand_solve(args):
        return solve(*args)
    solutions = multiprocessing.Pool().map(expand_solve, cases)

    # Print
    for case, solution in enumerate(solutions):
        print("Case #{}: {}".format(case + 1, solution))
