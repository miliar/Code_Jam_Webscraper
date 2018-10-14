#!/usr/bin/python

"""
Author: Morten Lied Johansen - mortenjo@ifi.uio.no

Google CodeJam 2011
Round: Qualifier
Problem: Magicka
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
            solvers.append(CaseSolver(casenr+1, *self.read_case_input(input)))
        if self.use_mp:
            p = Pool()
            solutions = p.map(run_in_process, solvers)
        else:
            solutions = map(run_in_process, solvers)
        for casenr, result in sorted(solutions):
            output.write("Case #%d: %s\n" % (casenr, result))
            output.flush()

    def read_combines(self, iterator):
        number_of_combines = int(iterator.next())
        combines = list()
        for i in range(number_of_combines):
            combines.append(iterator.next())
        combine_map = dict()
        for combine in combines:
            bases, result = combine[:2], combine[2]
            combine_map[tuple(bases)] = result
            combine_map[tuple(reversed(bases))] = result
        return combine_map

    def read_destroyers(self, iterator):
        number_of_destroyers = int(iterator.next())
        destroyers = list()
        for i in range(number_of_destroyers):
            destroyers.append(iterator.next())
        destroyer_map = dict()
        for destroyer in destroyers:
            self.add_destroyer(destroyer_map, destroyer[0], destroyer[1])
            self.add_destroyer(destroyer_map, destroyer[1], destroyer[0])
        return destroyer_map

    def add_destroyer(self, destroyer_map, destroyer, other):
        if not destroyer in destroyer_map:
            destroyer_map[destroyer] = set()
        destroyer_map[destroyer].add(other)

    def read_elements(self, iterator):
        number_of_elements = int(iterator.next())
        elements = list(iterator.next())
        assert number_of_elements == len(elements), "given number of elements (%d) does not match actual number read (%d)" % (number_of_elements, len(elements))
        elements.reverse()
        return elements

    def read_case_input(self, input):
        iterator = yield_line_of_items(input)
        combines = self.read_combines(iterator)
        destroyers = self.read_destroyers(iterator)
        elements = self.read_elements(iterator)
        return combines, destroyers, elements


class CaseSolver(object):
    def __init__(self, casenr, combines, destroyers, elements):
        self.casenr = casenr
        self.result = None
        self.combines = combines
        self.destroyers = destroyers
        self.elements = elements

    def _combine(self, element, tail):
        try:
            nonbase = self.combines[element,tail]
            self.result.pop()
            self.elements.append(nonbase)
            debug("%s and %s combined to form %s", element, tail, nonbase)
            return True
        except KeyError:
            pass
        return False

    def _destroy(self, element):
        try:
            badstuff = self.destroyers[element]
            for bad in badstuff:
                if bad in self.result:
                    self.result = [""]
                    debug("%s and %s destroyed the result", element, bad)
                    return True
        except KeyError:
            pass
        return False

    def solve(self):
        info("Solving case %d", self.casenr)
        debug("Combines: %s" % pformat(self.combines))
        debug("Destroyers: %s" % pformat(self.destroyers))
        debug("Elements: %s" % pformat(self.elements))
        self.result = [""]
        while len(self.elements):
            debug("Result so far: %r" % self.result)
            debug("Elements left: %r" % self.elements)
            element = self.elements.pop()
            tail = self.result[-1]
            if self._combine(element, tail):
                continue
            if self._destroy(element):
                continue
            self.result.append(element)
        self.result.pop(0)
        resultstring = "[%s]" % ", ".join(self.result)
        debug("Result: %s", resultstring)
        return self.casenr, resultstring

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
