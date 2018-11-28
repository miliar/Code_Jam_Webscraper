#!/usr/bin/env python
# encoding: utf-8
"""
Code Jam 2012

Author: Zach Bialecki
"""

import sys
import math
import getopt

help_message = "Enter the name of the input as the first argument"


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
	
	test_cases = parse_input(argv[1])
	output_list = compute(test_cases)
	output_result(output_list)


def parse_input(input_file):
	"""
	T = test cases
	G = number of buttons that need to be pushed
	R = robot color
	P = position
	"""
	test_cases = []

	with open(input_file, encoding='utf-8') as f:
		T = None
		G = None
		first_line = True

		for line in f:
			if first_line:
				T = int(line.strip())
				assert 1 <= T <= 30, "T is out of bounds"
				first_line = False
				
			else:
				G = line.strip()
				assert len(G) <= 100, "G is out of bounds"
				
				test_cases.append(list(G))
			
		assert len(test_cases) == T, "Number of lines in file did not match given N"
	return test_cases


def compute(test_cases):
	"""Compute the output for each test case"""
	output_list = []
	
	goog_str = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvyeqz"
	eng_str  = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upaozq"
	mapping  = build_mapping(list(goog_str), list(eng_str))

	for case in test_cases:
		translated = list(map(lambda x: mapping[x], case))
		output_list.append(''.join(translated))
		
	return output_list

def build_mapping(goog, eng):
	"""Build a hash from googlerese to english"""
	assert len(goog) == len(eng), "Strings are not the same length"

	mapping = {}
	for (g,e) in zip(goog, eng):
		if g in mapping:
			assert mapping[g] == e, "Inconsistent mapping"
		else:
			mapping[g] = e

	return mapping

def output_result(output_list):
	"""Print results to std out"""
	
	for i, result in enumerate(output_list):
		print("Case #{0}: {1}".format(i + 1, str(result)), end='\n')


if __name__ == "__main__":
	sys.exit(main())
