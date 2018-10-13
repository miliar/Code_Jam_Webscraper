# -*- coding: utf-8 -*-
# Google Code Jam - General utilities
# http://code.google.com/codejam/
# Copyright © 2012 Aluísio Augusto Silva Gonçalves
# This module is free software, licensed under the terms of the Artistic License 2.0


# Imports {{{1
##############

from __future__ import print_function, unicode_literals

import fileinput
import functools
import sys

if sys.platform == 'win32':
	from time import clock as time
else:
	from time import time


__all__ = ['TestCase', 'ProblemSolver']


# Test cases {{{1
#################

class TestCase(object):
	__slots__ = ('case_number', 'input', 'solution')

	def __init__ (self, nr):
		self.case_number = nr

	def __str__ (self):
		assert hasattr(self, 'solution'), "Called __str__ on uncomplete TestCase"
		return "Case #{}: {}".format(self.case_number, self.solution)

	def __hash__ (self):
		return self.case_number

	def solve (self, solver):
		""" Solve the test case by running the solver on the case's input. """
		self.solution = solver(self.input)
		return self


# Processing {{{1
#################

def parseInput (lines_by_case, f):
	""" Get test cases, reading `lines_by_case` lines of input for each one. """
	# Read test cases
	cases = []
	case_nr = int(f.readline().strip())
	for case_idx in range(case_nr):
		case = TestCase(case_idx + 1)
		case.input = []
		for line_idx in range(lines_by_case):
			case.input.append(f.readline().rstrip('\n'))
		cases.append(case)
	return cases

def getCases (parser):
	""" Get test cases, using `parser` to read input lines. """
	return parser(fileinput.input())

def processCases (cases, solver):
	""" Solve the test cases, one at a time. """
	return [case.solve(solver) for case in cases]

def processCasesAsyncMP (cases, solver):
	""" Solve the test cases, asynchronously, using multiple processes. """
	import multiprocessing
	pool = multiprocessing.Pool(5)
	solver = functools.partial(TestCase.solve, solver=solver)
	results = pool.map_async(solver, cases)
	results.wait()
	return results.get()

def processCasesAsyncF (cases, solver):
	""" Solve the test cases, asynchronously, using concurrent.futures. """
	import concurrent.futures
	with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
		futures = [executor.submit(processCase, case, solver) for case in cases]
	return [future.result() for future in concurrent.futures.as_completed(futures)]

def outputResults (cases):
	""" Print the cases' solutions, as required by the server. """
	for case in sorted(cases, key=lambda case: case.case_number):
		print(case)


# Entry point {{{1
##################

class ProblemSolver(object):
	def __init__ (self, module_name, input):
		self.autorun = (module_name == '__main__')
		if callable(input):
			self.input_parser = input
		elif isinstance(input, int):
			self.input_parser = functools.partial(parseInput, input)
		else:
			raise TypeError("Expecting callable or int, got {}".format(type(input)))

	def __call__ (self, func):
		self.solver = func
		self.__call__ = self.run
		if self.autorun: self.run()

	def run (self):
		# Read inputs
		start = time()
		cases = getCases(self.input_parser)
		end = time()
		print("Input reading time: {} seconds".format(end - start), file=sys.stderr)

		# Get solutions
		start = time()
		results = processCases(cases, self.solver)
		end = time()
		print("Data processing time: {} seconds".format(end - start), file=sys.stderr)

		# Print outputs
		start = time()
		outputResults(results)
		end = time()
		print("Output processing time: {} seconds".format(end - start), file=sys.stderr)
