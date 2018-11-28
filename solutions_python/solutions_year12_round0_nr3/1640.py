#!/usr/bin/python

"""
Author: Morten Lied Johansen - mortenjo@ifi.uio.no

Google CodeJam 2012
Round: Qualifier
Problem: Recycled numbers
"""

import os
import sys
import time
import itertools
import collections
from cStringIO import StringIO
import unittest
import logging
from logging import info, debug
from multiprocessing import Pool

# Set up basic logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)

def yield_line_of_items(reader):
    for x in reader.readline().strip().split():
        yield x

def read_line_of_items(reader):
    return list(yield_line_of_items(reader))

def yield_line_of_ints(reader):
    for i in yield_line_of_items(reader):
        yield int(i)

def read_line_of_ints(reader):
    return list(yield_line_of_ints(reader))

def yield_lines_of_items(reader, num=1):
    for i in range(num):
        yield read_line_of_items(reader)

def read_lines_of_items(reader, num=1):
    return list(yield_lines_of_ints(reader, num))

def yield_lines_of_ints(reader, num=1):
    for i in range(num):
        yield read_line_of_ints(reader)

def read_lines_of_ints(reader, num=1):
    return list(yield_lines_of_ints(reader, num))

def run_in_process(case_solver):
    return case_solver.solve()

def memoizing(func):
    """Function decorator to cache a function's output."""
    memos = dict()
    def memoize(*args):
        if args in memos:
            return memos[args]
        res = func(*args)
        memos[args] = res
        return res
    return memoize

class Solver(object):
    def __init__(self, input_name, use_mp=False):
        self.input_name = input_name
        self.output_name = self._make_output_name()
        self.use_mp = use_mp

    def _make_output_name(self):
        basename, ext = os.path.splitext(self.input_name)
        output_name = basename + ".out"
        return output_name

    def open_output(self):
        return open(self.output_name, "w")

    def open_input(self):
        return open(self.input_name, "r")

    def main(self):
        input = self.open_input()
        output = self.open_output()
        self.solve(input, output)

    def solve(self, input, output):
        number_of_cases = read_line_of_ints(input)[0]
        solvers = list()
        for casenr in xrange(number_of_cases):
            solvers.append(CaseSolver(casenr+1, *self.read_case_input(input)))
        if self.use_mp:
            p = Pool()
            solutions = p.map(run_in_process, solvers)
        else:
            solutions = map(run_in_process, solvers)
        for casenr, result in sorted(solutions):
            output.write("Case #%d: %s\n" % (casenr, result))
            output.flush()

    def read_case_input(self, input):
        return read_line_of_ints(input)

class CaseSolver(object):
    def __init__(self, casenr, lower_bound, upper_bound):
        self.casenr = casenr
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.visited = set()

    def solve(self):
        info("Solving case %d", self.casenr)
        pairs = set()
        for i in xrange(self.lower_bound, self.upper_bound+1):
            if i in self.visited:
                continue
            values = generate_values(i)
            debug("Values: %r", values)
            values = self.filter_values(values)
            debug("Filtered values: %r", values)
            if len(values) > 1:
                self.visited.update(values)
                pairs.update(find_combinations(values))
            debug("Visited %d values so far", len(self.visited))
        result = len(pairs)
        debug("Result: %s", result)
        return self.casenr, result

    def filter_values(self, values):
        return frozenset(x for x in values if self.lower_bound <= x <= self.upper_bound)

@memoizing
def generate_values(i):
    deque = collections.deque(str(i))
    values = set()
    for i in xrange(len(deque)):
        deque.rotate(1)
        value = int("".join(deque))
        if value != i:
            values.add(value)
    return frozenset(values)

def find_combinations(values):
    return tuple(itertools.combinations(sorted(values), 2))

# === Verify correctness of sample data
class SampleTester(unittest.TestCase):
    def setUp(self):
        self.data = open("sample.correct", "r").read()
    def test_sample(self):
        output = StringIO()
        solver = Solver("sample.in")
        input = solver.open_input()
        solver.solve(input, output)
        self.assertEqual(self.data, output.getvalue())

if __name__ == "__main__":
    if "--debug" in sys.argv:
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.DEBUG)
    use_mp = False
    if "--use-mp" in sys.argv:
        use_mp = True
    input_name = sys.argv[1]
    if input_name == "test":
        suite = unittest.TestLoader().loadTestsFromTestCase(SampleTester)
        unittest.TextTestRunner(verbosity=2).run(suite)
    else:
        start = time.time()
        solver = Solver(input_name, use_mp)
        solver.main()
        end = time.time()
        info("Time spent: %s" % time.strftime("%M minutes, %S seconds", time.gmtime(end-start)))
