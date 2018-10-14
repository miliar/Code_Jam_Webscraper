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
    N = inputfile.read_int()
    return (N, )


def solve(n):
    digits = [x for x in str(n)]
    res = digits
    changed = True
    while changed:
        changed = False
        for i in xrange(len(digits)-1):
            if digits[i] > digits[i+1] and digits[i] != "0":
                digits[i] = str(int(digits[i]) - 1)
                digits[i+1:] = "9" * (len(digits) - i - 1)
                changed = True
                break

    if digits[0] != "0":
        assert int("".join(res)) <= n
        return "".join(res)
    else:
        return "".join("9" * (len(digits) - 1))

assert solve(7) == "7"
assert solve(132) == "129"
assert solve(352) == "349"
assert solve(480) == "479"
assert solve(1000) == "999"
assert solve(8245) == "7999"
assert solve(2853684203540062) == "2799999999999999"
assert solve(111111111111111110) == "99999999999999999"

for n in xrange(1, 10000 + 10):
    res = n
    invalid = True
    while invalid:
        digits = [x for x in str(res)]
        invalid = False
        for i in xrange(len(digits)-1):
            if digits[i] > digits[i+1]:
                invalid = True
                res -= 1
                break
    assert solve(n) == str(res)

def write(result):
    print "{}".format(result)


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
    if verbose:
        sys.stderr.write("\n")
        sys.stderr.flush()

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
