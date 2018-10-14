#!/usr/bin/python
# -*- coding: utf-8

"""
Author: Morten Lied Johansen - mortenjo@ifi.uio.no

Google CodeJam 2013
Round: Qualifier
Problem: Tic-Tac-Toe-Tomek
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
        board = []
        for i in xrange(4):
            board.append(list(input.readline().strip()))
        input.readline()
        return board


def flip(rows):
    columns = []
    for i in xrange(len(rows[0])):
        column = []
        for row in rows:
            column.append(row[i])
        columns.append(column)
    return columns


def diagonals(rows):
    result = [
        [rows[i][i] for i in xrange(len(rows[0]))],
        [rows[i][len(rows[0])-1-i] for i in xrange(len(rows[0]))]
    ]
    return result


class CaseSolver(object):
    def __init__(self, casenr, board):
        self.casenr = casenr
        self.to_check = board
        self.to_check.extend(flip(board))
        self.to_check.extend(diagonals(board))
        self.cells = "".join(("".join(row) for row in board))

    def solve(self):
        info("Solving case %d", self.casenr)
        if self.check_for_win("O"):
            result = "X won"
        elif self.check_for_win("X"):
            result = "O won"
        elif "." in self.cells:
            result = "Game has not completed"
        else:
            result = "Draw"
        debug("Result: %s", result)
        return self.casenr, result

    def check_for_win(self, loser):
        for line in self.to_check:
            if "." in line: continue
            if loser in line: continue
            return True

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
