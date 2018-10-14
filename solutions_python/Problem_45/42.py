#!/usr/bin/env python

import sys
import itertools


def jail(num_cells, freemans):
    cells = set(range(1, num_cells + 1))
    costs = [gold_cost(cells, seq) for seq in permutations(freemans)]
    return min(costs)

def gold_cost(cells, free_seq):
    # Clone cells set
    cells = set(cells)
    cost = 0
    for p in free_seq:
        cells.remove(p)
        neighbors = count_neighbors(cells, p, 1) + count_neighbors(cells, p, -1)
        cost += neighbors
    return cost

def count_neighbors(cells, p, direction=1):
    neighbor = p
    count = 0
    while True:
        neighbor = neighbor + direction
        if neighbor in cells:
            count += 1
        else:
            break
    return count
    
# From http://docs.python.org/library/itertools.html#itertools.permutations
# Included in python 2.6
def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return


if __name__ == "__main__":
    cases = int(sys.stdin.next())
    for i in xrange(1, cases + 1):
        cells, _ = [int(j) for j in sys.stdin.next().strip().split()]
        freemans = [int(j) for j in sys.stdin.next().strip().split()]
        answer = jail(cells, freemans)
        print "Case #%d: %s" % (i, answer)
	
