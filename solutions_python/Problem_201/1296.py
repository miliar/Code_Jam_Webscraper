#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import division
import sys
from multiprocessing import Pool
#from pulp import *
#from z3 import *
from collections import namedtuple
import math

verbose = True


def read(inputfile):
    N, K = inputfile.read_integers()
    return (N, K)


def solve(N, K):
    K_orig = K
    small_val = N
    count_small = 1
    count_big = 0
    caso = ""

    while K > 0 and small_val > 0:
        new_small_val = (small_val - 1) // 2
        new_count_small = 0
        new_count_big = 0
        if small_val % 2 == 0:
            # Dividi i big
            new_count_big += 2 * count_big
            K -= count_big
            caso = "A"
            if K > 0:
                # Dividi gli small
                new_count_small += count_small
                new_count_big += count_small
                K -= count_small
                caso = "B"
        else:
            # Dividi i big
            new_count_small += count_big
            new_count_big += count_big
            K -= count_big
            caso = "B"
            if K > 0:
                # Dividi gli small
                new_count_small += 2 * count_small
                K -= count_small
                caso = "C"
        # Aggiorna
        small_val = new_small_val
        count_small = new_count_small
        count_big = new_count_big

    if K > 0 and small_val == 0:
        #print "base"
        K -= count_big
        count_small = 0
        count_big = count_big
        caso = "A"
        small_val = -1

    assert K <= 0

    if caso == "C":
        if count_small == 0:
            assert small_val == 0
        res = (small_val, small_val)
    elif caso == "A":
        assert count_small == 0
        assert count_big > 0
        res = (small_val + 1, small_val + 1)
    else:
        assert caso == "B"
        res = (small_val + 1, small_val)

    return res

assert solve(22, 15) == (0, 0)

assert solve(1, 1) == (0, 0)
assert solve(2, 1) == (1, 0)
assert solve(3, 1) == (1, 1)
assert solve(4, 1) == (2, 1)
assert solve(5, 1) == (2, 2)
assert solve(2, 2) == (0, 0)
assert solve(3, 2) == (0, 0)
assert solve(4, 2) == (1, 0)
assert solve(5, 2) == (1, 0)
assert solve(6, 2) == (1, 1)
assert solve(7, 2) == (1, 1)
assert solve(3, 3) == (0, 0)
assert solve(4, 3) == (0, 0)
assert solve(5, 3) == (1, 0)
assert solve(6, 3) == (1, 0)
assert solve(7, 3) == (1, 1)
assert solve(8, 3) == (1, 1)
assert solve(5, 4) == (0, 0)
assert solve(11, 8) == (0, 0)
assert solve(10, 3) == (2, 1)
assert solve(10, 4) == (1, 0)
assert solve(10, 5) == (1, 0)
assert solve(22, 1) == (11, 10)
assert solve(22, 2) == (5, 5)
assert solve(22, 3) == (5, 4)
assert solve(22, 4) == (2, 2)
assert solve(22, 5) == (2, 2)
assert solve(22, 6) == (2, 2)
assert solve(22, 7) == (2, 1)
assert solve(22, 8) == (1, 0)
assert solve(22, 9) == (1, 0)
assert solve(22, 14) == (1, 0)
assert solve(22, 15) == (0, 0)
assert solve(22, 16) == (0, 0)
assert solve(22, 17) == (0, 0)
assert solve(22, 18) == (0, 0)
assert solve(22, 19) == (0, 0)
assert solve(22, 20) == (0, 0)
assert solve(22, 21) == (0, 0)
assert solve(22, 22) == (0, 0)
assert solve(1000, 1000) == (0, 0)
assert solve(1000, 1) == (500, 499)

for n in xrange(1, 1000):
    assert solve(n, 1) == (n // 2, (n-1) // 2)
    assert solve(n, n) == (0, 0)
    assert solve(2*n, n) == (1, 0)

for n in xrange(1, 500):
    for k in xrange(1, n):
        res = solve(n, k)
        assert k + res[0] <= n

def write(result):
    print "{} {}".format(*result)


def main(parallel, _verbose):
    global verbose
    verbose = _verbose

    # Read
    inputfile = FileParser()
    T = inputfile.read_int()
    log("Solving", T, "test cases")
    test_cases = [read(inputfile) for _ in xrange(T)]

    # Solve
    if parallel:
        process_pool = Pool(processes=4)
        test_results = process_pool.map_async(solve_data, test_cases).get(9999999)
    else:
        test_results = map(solve_data, test_cases)

    # Write
    for i, result in enumerate(test_results):
        print "Case #{}:".format(i + 1),
        write(result)


def solve_data(data):
    res = solve(*data)
    if verbose:
        sys.stderr.write(".")
        sys.stderr.flush()
    return res


def log(*args):
    if verbose:
        print >> sys.stderr, " ".join(map(str, args))


class FileParser(object):
    """Read numbers/strings from file (or stdin by default), one line by one.

    Example:
        inputfile = FileParser()
        # Read a line of 5 integers
        R, S, U, P, M = inputfile.readIntegers()
        inputfile.close()
    """

    def __init__(self, filepath=None):
        if filepath is None:
            self.fd = sys.stdin
        else:
            self.fd = open(filepath)

    def read_lines(self):
        return self.fd.readlines()

    def read_string(self):
        return self.fd.readline().rstrip()

    def read_strings(self):
        return [x for x in self.read_string().split()]

    def read_int(self):
        return int(self.fd.readline())

    def read_integers(self):
        return [int(x) for x in self.fd.readline().split()]

    def read_float(self):
        return float(self.fd.readline())

    def read_floats(self):
        return [float(x) for x in self.fd.readline().split()]

    def close(self):
        if self.fd is not sys.stdin:
            self.fd.close()
        self.fd = None


if __name__ == "__main__":
    main("-s" not in sys.argv, "-q" not in sys.argv)
