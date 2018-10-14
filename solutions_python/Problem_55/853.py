#!/usr/bin/python

import os
import sys

USAGE = "Usage: python %s INPUT_FILE" % (sys.argv[0])

def main(argv=None):
	if argv is None:
		argv = sys.argv
	
	if len(argv) != 2:
		print USAGE
		return 1
	
	input_filename = argv[1]
	
	params = InputParameters(input_filename)
	
	i = 1
	for test_case in params.test_case_list:
		print "Case #%d: %d" % (i, test_case.compute_revenue())
		i += 1

class TestCase:
	def __init__(self):
		self.R = None
		self.k = None
		self.N = None
		self.group_list = []
	
	def compute_revenue(self):
		if (self.R is None or
		    self.k is None or
		    self.N is None or
		    len(self.group_list) < 1):
			return 0
		
		revenue = 0
		
		# Caches the revenue generated and the number of groups on a trip for
		# a given permutation of the group list
		memoized_revenue = {}
		
		for i in range(0, self.R):
			group_list_permutation = tuple(self.group_list)
			if group_list_permutation in memoized_revenue:
				revenue += memoized_revenue[group_list_permutation][0]
				passenger_group_list = self.group_list[0:memoized_revenue[group_list_permutation][1]]
				del self.group_list[0:memoized_revenue[group_list_permutation][1]]
				self.group_list += passenger_group_list
				continue
			
			group_count = 0
			passenger_count = 0
			passenger_group_list = []
			for j in range(0, self.N):
				if len(self.group_list) == 0:
					break;
				temp_sum = passenger_count + self.group_list[0]
				if temp_sum > self.k:
					break;
				passenger_count = temp_sum
				passenger_group_list.append(self.group_list.pop(0))
				group_count = j + 1
			marginal_revenue = sum(passenger_group_list)
			revenue += marginal_revenue
			self.group_list += passenger_group_list
			memoized_revenue[group_list_permutation] = (marginal_revenue, group_count)
		return revenue

class InputParameters:
	def __init__(self, input_filename=None):
		self.T = None
		self.test_case_list = []
		
		if input_filename is not None:
			self.parse_input_file(input_filename)
	
	def parse_input_file(self, input_filename):
		if not os.path.exists(input_filename):
			return -1
		elif not os.path.isfile(input_filename):
			return -2
		
		input_file = open(input_filename, "r")
		lines = [l.rstrip() for l in input_file.readlines()]
		
		if len(lines) < 1:
			return -3
		
		self.T = int(lines[0])
		
		for i in range(1, self.T*2, 2):
			test_case = TestCase()
			test_case.R, test_case.k, test_case.N = tuple([int(l) for l in lines[i].split()])
			test_case.group_list = [int(l) for l in lines[i+1].split()]
			self.test_case_list.append(test_case)
		
		input_file.close()
		return 0

if __name__ == "__main__":
	sys.exit(main())

