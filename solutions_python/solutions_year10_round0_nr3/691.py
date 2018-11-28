#!/usr/bin/python

import os
import sys
import time

from collections import deque
from cStringIO import StringIO
from cProfile import run
import unittest

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
        self.pre_solved = dict()
        self.cycle_tracker = dict()
        number_of_cases = read_line_of_ints(input)[0]
        for casenr in xrange(number_of_cases):
            print "Solving case %d" % (casenr+1)
            result = self.solve_case(*self.read_case_input(input))
            output.write("Case #%d: %s\n" % (casenr + 1, result))
            output.flush()

    def read_case_input(self, input):
        rounds, capacity, number_of_groups = read_line_of_ints(input)
        groups = read_line_of_ints(input)
        return (rounds, capacity, groups)

    def solve_case(self, rounds, capacity, groups):
        start = time.time()
        total_income = 0
        queue = tuple(groups)
        fill = self.fill_coaster
        round = 0
        while round < rounds:
            if (round+1) % 100000 == 0:
                print "Round %d of %d" % (round+1, rounds)
                print "Total income so far: %d" % total_income
                print "Time spent: %s" % time.strftime("%M minutes, %S seconds", time.gmtime(time.time()-start))
            key = (capacity, queue)
            try:
                result = self.pre_solved[key]
                for cycle_point in self.cycle_tracker[key]:
                    #print "Checking %s for jump possibility" % repr(cycle_point)
                    jump_rounds = round - cycle_point[0]
                    jump_income = total_income - cycle_point[1]
                    if (round + jump_rounds) < rounds:
                        #print "Jumping %d rounds at round %d" % (jump_rounds, round)
                        round += jump_rounds
                        total_income += jump_income
                        break
            except KeyError:
                result = fill(capacity, queue)
                self.pre_solved[key] = result
            if key not in self.cycle_tracker:
                self.cycle_tracker[key] = list()
            self.cycle_tracker[key].append((round, total_income))
            income, queue = result
            total_income += income
            round += 1
        print "Round %d of %d" % (round+1, rounds)
        print "Total income so far: %d" % total_income
        print "Time spent: %s" % time.strftime("%M minutes, %S seconds", time.gmtime(time.time()-start))
        return str(total_income)

    def fill_coaster(self, capacity, queue):
        max = len(queue)
        boarded = 0
        boarded_groups = deque()
        queue = deque(queue)
        q_pop = queue.popleft
        q_ap = queue.appendleft
        b_ap = boarded_groups.append
        for i in xrange(max):
            group = q_pop()
            if boarded + group > capacity:
                q_ap(group)
                break
            boarded += group
            b_ap(group)
        queue.extend(boarded_groups)
        return boarded, tuple(queue)

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
    input_name = sys.argv[1]
    if input_name == "test":
        suite = unittest.TestLoader().loadTestsFromTestCase(SampleTester)
        unittest.TextTestRunner(verbosity=2).run(suite)
    else:
        start = time.time()
        solver = Solver(input_name)
        run("solver.main()", "profile")
        end = time.time()
        print "Time spent: %s" % time.strftime("%M minutes, %S seconds", time.gmtime(end-start))
