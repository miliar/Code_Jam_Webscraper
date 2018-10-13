# Written by Nikolai Artemiev

import collections
import functools
import itertools
import math
import multiprocessing
import os
import resource
import sys
pi = math.pi

def solve(N, K, P):
    M = 0
    for b in range(N):
        AB = P[b][0] ** 2 * pi + (P[b][1] * P[b][0] * pi * 2)
        PA = [(p[1] * p[0] * pi * 2) for p in (P[:b] + P[b + 1:])]
        PA = sorted(PA, key = lambda x: -x)
        AB += sum(PA[:K - 1])
        M = max(M, AB)
    return M




def read(F):
    N, K =  [int(num) for num in F.readline().split()]
    P =  [[int(num) for num in F.readline().split()] for n in range(N)]
    return N, K, P

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

    solutions = multiprocessing.Pool().map(expand_solve, cases)

    # Print
    for case, solution in enumerate(solutions):
        print("Case #{}: {}".format(case + 1, solution))
