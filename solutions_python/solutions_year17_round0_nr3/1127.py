#!/usr/bin/env python

################################################################################
#
# Google Code Jam - 2017
#
# Qualification round - Problem C - Bathroom Stalls
#
# Joaquin Derrac - carrdelling@gmail.com
#
################################################################################

import sys
import heapq as hp
import functools


@functools.lru_cache(maxsize=None)
def break_space(size):

    if size % 2 == 1:
        n = (size-1) / 2
        return n, n
    else:
        n = size / 2
        return n, n-1


def solve(size, people):
    """  Solve the problem """

    # heapq only provides a minheap -
    # so all sizes will be negative inside the heap

    space = [-size]

    n, m = size, size
    for _ in range(people):

        largest = -hp.heappop(space)

        n, m = break_space(largest)

        hp.heappush(space, -n)
        hp.heappush(space, -m)

    return int(n), int(m) if n >= m else int(m), int(n)

input_path = sys.argv[1]

with open(input_path) as input_file:

    n_cases = int(input_file.readline().strip())

    for case in range(1, n_cases+1):
        N, K = map(int, input_file.readline().strip().split())
        solution = solve(N, K)
        print ('Case #{0}: {1} {2}'.format(case, solution[0], solution[1]))
