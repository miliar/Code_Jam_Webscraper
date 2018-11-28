# Written by Nikolai Artemiev

import collections
import functools
import itertools
import math
import multiprocessing
import os
import resource
import sys


def solve(N, Q, H, P, U):
    P = [max(p) for p in P]

    def s2(a, b, c):
        return s(a, b, c)

    @functools.lru_cache(maxsize = None)
    def s(C, r = None, s = None):
        if C == N - 1:
            return 0

        if C == 0:
            r, s = H[C][0], H[C][1]

        d = P[C]
        pc = d / float(s)

        sw = s2(C + 1, H[C + 1][0], H[C + 1][1])

        if r - d >= P[C + 1]:
            sw = min(sw, s2(C + 1, r - d, s))

        return pc + sw

    return s(0)



def read(F):
    N, Q = [int(num) for num in F.readline().split()]
    H = [[int(num) for num in F.readline().split()] for i in range(N)]
    P = [[int(num)for num in F.readline().split()] for i in range(N)]
    U = [[int(num) for num in F.readline().split()] for i in range(Q)]
    return N, Q, H, P, U


if __name__ == "__main__":
    # Resize stack to useful size
    recursion_limit = 100000
    resource.setrlimit(resource.RLIMIT_STACK, [resource.RLIM_INFINITY, resource.RLIM_INFINITY])
    sys.setrecursionlimit(recursion_limit)

    if "--input" in sys.argv and len(sys.argv) >= sys.argv.index("--input"):
        # Use input file from command line args
        input_file = sys.argv[sys.argv.index("--input") + 1]
    else:
        # Find the most recently downloaded input file
        input_files = [name for name in os.listdir(".") if name.endswith(".in")]
        input_file = max(input_files, key = os.path.getmtime)

    # Read cases
    with open(input_file) as F:
        T = int(F.readline())
        cases = [read(F) for case in range(T)]

    # Solve
    def expand_solve(args): return solve(*args)

    solutions = multiprocessing.Pool(1).map(expand_solve, cases)

    # Print
    for case, solution in enumerate(solutions):
        print("Case #{}: {}".format(case + 1, solution))
