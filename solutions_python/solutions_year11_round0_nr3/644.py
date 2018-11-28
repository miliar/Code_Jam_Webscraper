#!/usr/bin/python

"""
Author: Morten Lied Johansen - mortenjo@ifi.uio.no

Google CodeJam 2011
Round: Qualifier
Problem: Candy Splitting
"""

import os
import sys
import time
from pprint import pformat
from cStringIO import StringIO
import unittest
import logging
from logging import info, debug, error
from multiprocessing import Pool

# Set up basic logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)

def memoizing_list(func):
    """Function decorator to cache a function's output."""
    memos = dict()
    def memoize(self, arg):
        key = tuple(sorted(arg))
        if key in memos:
            debug("getting %r from cache", key)
            return memos[key]
        res = func(self, arg)
        memos[key] = res
        return res
    return memoize

def memoize_2list(func):
    memos = dict()
    def memoize(self, arg1, arg2):
        key = tuple(sorted(arg1)),tuple(sorted(arg2))
        if key in memos:
            debug("getting %r from cache", key)
            return memos[key]
        res = func(self, arg1, arg2)
        memos[key] = res
        return res
    return memoize

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
            solvers.append(CaseSolver(casenr+1, self.read_case_input(input)))
        if self.use_mp:
            p = Pool()
            solutions = p.map(run_in_process, solvers)
        else:
            solutions = map(run_in_process, solvers)
        for casenr, result in sorted(solutions):
            output.write("Case #%d: %s\n" % (casenr, result))
            output.flush()

    def read_case_input(self, input):
        number_of_candies = read_line_of_ints(input)[0]
        candy_values = read_line_of_ints(input)
        return candy_values

class CaseSolver(object):
    def __init__(self, casenr, candy_values):
        self.casenr = casenr
        self.result = None
        self.candy_values = sorted(candy_values)

    @memoizing_list
    def value_of_pile(self, pile):
        value = 0
        for candy in pile:
            value ^= candy
        return value

    @memoizing_list
    def real_value(self, pile):
        value = 0
        for candy in pile:
            value += candy
        return value

    @memoize_2list
    def solve_for(self, remaining, pile):
        debug("Evaluating remaining: %r with already split %r", remaining, pile)
        for candy in remaining:
            suggestion = list(pile)
            suggestion.append(candy)
            leftover = list(remaining)
            leftover.remove(candy)
            if suggestion and leftover:
                debug("Attempting pile %r and leftover %r", suggestion, leftover)
                if self.value_of_pile(suggestion) == self.value_of_pile(leftover):
                    debug("Success!")
                    return self.real_value(leftover)
                result = self.solve_for(leftover, suggestion)
                if result:
                    return result
        return 0

    def solve(self):
        info("Solving case %d", self.casenr)
        self.result = self.solve_for(self.candy_values[:], list())
        if not self.result:
            self.result = "NO"
        debug("Result: %s", self.result)
        return self.casenr, self.result

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
    use_mp = True
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
