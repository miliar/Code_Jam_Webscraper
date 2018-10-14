#!/usr/bin/env python
# -*- coding: utf-8

"""
Author: Morten Lied Johansen - mortenjo@ifi.uio.no

Google CodeJam 2013
Round: Qualifier
Problem: Fair and Square
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
import math
import cPickle

PICKLE_FILE_NAME = "fair_and_square.pickle"

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
        fair_and_square = self.load_fair_and_square()
        number_of_cases = read_line_of_ints(input)[0]
        solvers = list()
        for casenr in xrange(number_of_cases):
            solvers.append(CaseSolver(casenr+1, fair_and_square, *self.read_case_input(input)))
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

    def load_fair_and_square(self):
        with open(PICKLE_FILE_NAME, "rb") as fobj:
            return cPickle.load(fobj)


class CaseSolver(object):
    def __init__(self, casenr, fair_and_square, lower, upper):
        self.casenr = casenr
        self.lower = lower
        self.upper = upper
        self.fair_and_square = fair_and_square

    def solve(self):
        info("Solving case %d", self.casenr)
        in_range = [candidate for candidate in self.fair_and_square if candidate >= self.lower and candidate <= self.upper]
        result = str(len(in_range))
        debug("Result: %s", result)
        return self.casenr, result

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


def generate(limit):
    wanted = generate_fair_and_square_numbers(limit)
    with open(PICKLE_FILE_NAME, "wb") as fobj:
        cPickle.dump(wanted, fobj)


def generate_fair_and_square_numbers(limit):
    p = Pool()
    math_sqrt = math.sqrt(limit)
    rounded = int(round(math_sqrt))
    numbers_to_check = xrange(rounded)
    wanted = [x for x in p.map(check_number, numbers_to_check) if x]
    return wanted


def check_number(number):
    if number % 1000000 == 0:
        print "Checking %d" % number
    if is_fair(number):
        square = number * number
        if is_fair(square):
            return square
    return None


def is_fair(number):
    number_as_string = str(number)
    rev = "".join(reversed(number_as_string))
    return rev == number_as_string


if __name__ == "__main__":
    if "--debug" in sys.argv:
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.DEBUG)
    use_mp = False
    if "--use-mp" in sys.argv:
        use_mp = True
    input_name = sys.argv[1]
    if input_name == "generate":
        generate(10**14)
    elif input_name == "test":
        suite = unittest.TestLoader().loadTestsFromTestCase(SampleTester)
        unittest.TextTestRunner(verbosity=2).run(suite)
    else:
        start = time.time()
        solver = Solver(input_name, use_mp)
        solver.main()
        end = time.time()
        info("Time spent: %s" % time.strftime("%M minutes, %S seconds", time.gmtime(end-start)))


if __name__ == "__main__":
    pass
