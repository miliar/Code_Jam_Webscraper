#!/usr/bin/python

"""
Author: Morten Lied Johansen - mortenjo@ifi.uio.no

Google CodeJam 2010
Round: 1C
Problem: A
"""

import os
import sys
import time
from cStringIO import StringIO
import unittest
import logging
from logging import info, debug, error

# Set up basic logging
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)

# Code from http://www.bryceboe.com/2006/10/23/line-segment-intersection-algorithm/
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

def ccw(A, B, C):
	return (C.y-A.y) * (B.x-A.x) > (B.y-A.y) * (C.x-A.x)

def intersect(A, B, C, D):
	return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)
# ===================

class Line(object):
    def __init__(self, left_y, right_y):
        self.left = Point(0, left_y)
        self.right = Point(1, right_y)

    def intersects(self, other):
        return intersect(self.left, self.right, other.left, other.right)

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

class Solver(object):
    def __init__(self, input_name):
        self.input_name = input_name
        self.output_name = self._make_output_name()

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
        for casenr in xrange(number_of_cases):
            info("Solving case %d" % (casenr + 1))
            result = self.solve_case(self.read_case_input(input))
            info("Result: %s", result)
            output.write("Case #%d: %s\n" % (casenr + 1, result))
            output.flush()

    def read_case_input(self, input):
        number_of_lines = int(input.readline().strip())
        lines = list()
        for i in range(number_of_lines):
            lines.append(Line(*read_line_of_ints(input)))
        return lines

    def solve_case(self, lines):
        count = 0
        for i, line in enumerate(lines):
            for other in lines[i:]:
                count += int(line.intersects(other))
        return count

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
    input_name = sys.argv[1]
    if input_name == "test":
        suite = unittest.TestLoader().loadTestsFromTestCase(SampleTester)
        unittest.TextTestRunner(verbosity=2).run(suite)
    else:
        start = time.time()
        solver = Solver(input_name)
        solver.main()
        end = time.time()
        print "Time spent: %s" % time.strftime("%M minutes, %S seconds", time.gmtime(end-start))
