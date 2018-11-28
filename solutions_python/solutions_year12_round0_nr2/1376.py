#!/usr/bin/env python
# encoding: utf-8
"""
Code Jam 2011

Author: Zach Bialecki
"""

import sys
import math
import getopt

help_message = "Enter the name of the input as an argument"


class Usage(Exception):
	def __init__(self, msg):
		self.msg = msg


def main(argv = None):
	"""Parse command line arguments and run the program"""
	if argv is None:
		argv = sys.argv
	try:
		try:
			opts, args = getopt.getopt(argv[1:], "h", ["help"])
		except getopt.error:
			raise Usage(help_message)
		
		# option processing
		for option, value in opts:
			if option in ("-h", "--help"):
				raise Usage(help_message)
	
	except (Usage, err):
		print >> sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
		print >> sys.stderr, "\t for help use --help"
		return 2
	
	test_cases  = parse_input(argv[1])
	output_list = compute(test_cases)
	output_result(output_list)


def parse_input(input_file):
	"""
	T = test cases
	N = number of googlers
	S = number of surprising results
	p = lower bound
	"""
	with open(input_file, encoding='utf-8') as f:
		T = None
		first_line = True
		test_cases = []
		
		for line in f:
			if first_line:
				T = int(line.strip())
				assert 1 <= T <= 100, "N is out of bounds"
				first_line = False
				
			else:
				N, S, p, *scores = line.split()
				N = int(N)
				S = int(S)
				p = int(p)
				assert len(scores) == N, "Number of scores doesn't match N"
				assert 0 <= S <= N, "S is out of bounds"
				assert 0 <= p <= 10, "Lower limit is out of bounds"
				
				totals = list(map(int, scores))
				case = { 'S': S, 'p': p, 'totals': totals }
				test_cases.append(case)
			
		assert len(test_cases) == T, "Number of lines in file did not match given N"
	return test_cases


def compute(test_cases):
	"""Compute the output for each test case"""
	output_list = []
	
	for case in test_cases:
		S = case['S']
		num = 0

		diff1 = case['p'] - 1
		diff2 = case['p'] - 2

		if diff1 < 0:
			diff1 = 0
		if diff2 < 0:
			diff2 = 0

		for ti in case['totals']:
			# Non-surprising case 
			if (ti - case['p'] - 2*diff1 >= 0):
				num += 1
			# Surprising case 
			elif (ti - case['p'] - 2*diff2 >= 0) and S > 0:
				num += 1
				S -= 1

		output_list.append(num)
		
	return output_list


def output_result(output_list):
	"""Print results to std out"""
	
	for i, result in enumerate(output_list):
		print("Case #{0}: {1}".format(i + 1, str(result)), end='\n')


if __name__ == "__main__":
	sys.exit(main())
