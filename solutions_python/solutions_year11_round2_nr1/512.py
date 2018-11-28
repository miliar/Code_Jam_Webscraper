#!/usr/bin/python

"""
Author: Morten Lied Johansen - mortenjo@ifi.uio.no

Google CodeJam 2011
Round: Round 1B
Problem: RPI
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
        number_of_teams = read_line_of_ints(input)[0]
        team_results = list()
        for t in xrange(number_of_teams):
            results = list(input.readline().strip())
            team_results.append(results)
        return team_results

def average(numbers):
    return sum(numbers) / len(numbers)
    
class CaseSolver(object):
    def __init__(self, casenr, team_results):
        self.casenr = casenr
        self.team_results = team_results
        self.team_wp = dict()
        self.team_owp = dict()
        self.team_oowp = dict()

    def calculate_wp(self, team_number):
        results = self.team_results[team_number]
        wp = self._calculate_wp(results)
        self.team_wp[team_number] = wp

    def _calculate_wp(self, results):
        wins = 0.0
        losses = 0.0
        for r in results:
            if r == "1":
                wins += 1
            elif r == "0":
                losses += 1
        wp = wins/(wins+losses)
        return wp

    def calculate_owp(self, team_number):
        results = self.team_results[team_number]
        opponents = list()
        for i, r in enumerate(results):
            if r != ".": opponents.append(i)
        wps = list()
        for opponent in opponents:
            their_results = list(self.team_results[opponent])
            del their_results[team_number]
            their_wp = self._calculate_wp(their_results)
            wps.append(their_wp)
        self.team_owp[team_number] = average(wps)
    
    def calculate_oowp(self, team_number):
        results = self.team_results[team_number]
        owps = list()
        for i, r in enumerate(results):
            if r != ".":
                owps.append(self.team_owp[i])
        self.team_oowp[team_number] = average(owps)

    def calculate_rpi(self, team_number):
        wp = self.team_wp[team_number]
        owp = self.team_owp[team_number]
        oowp = self.team_oowp[team_number]
        return 0.25 * wp + 0.50 * owp + 0.25 * oowp

    def team_result(self, team_number):
        return "%.12f" % self.calculate_rpi(team_number)
    
    def solve(self):
        info("Solving case %d", self.casenr)
        for team_number in xrange(len(self.team_results)):
            self.calculate_wp(team_number)
        for team_number in xrange(len(self.team_results)):
            self.calculate_owp(team_number)
        for team_number in xrange(len(self.team_results)):
            self.calculate_oowp(team_number)
        results = [""]
        for team_number in xrange(len(self.team_results)):
            results.append(self.team_result(team_number))
        result = "\n".join(results)
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
