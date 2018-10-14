#!/usr/bin/python

#imports
from sys import argv, exit
from math import sqrt

#classes
class case(object):
	def __init__(self, limits):
		""" Create the case and store it's lower and upper limit."""
		self.low = limits[0]
		self.high = limits[1]
		self.squares = []
		self.square_palindromes = []
		self.fair_squares = []
	
	def find_squares(self):
		"""Create a list of squares in the range of low-high inclusive"""
		self.squares = [x for x in range(self.low, self.high + 1) if sqrt(x) == int(sqrt(x))]
		
	def find_palindromes(self):
		""" Create a list of the squares that are also palindromes"""
		self.square_palindromes = [x for x in self.squares if self.is_palindrome(x)]
	
	def find_fair_squares(self):
		""" Create a list of the square palindromes that are the square
		of a palindrome"""
		self.fair_squares = [x for x in self.square_palindromes if self.is_palindrome(int(sqrt(x)))]
	
	def is_palindrome(self, test, debug=False):
		if debug:
			print str(test), str(test)[::-1]
		return str(test) == str(test)[::-1]
		
	def print_info(self):
		"""For debugging"""
		print "Low: {}. High: {}".format(self.low, self.high)
		print "Squares: {}".format(self.squares)
		print "Palindrome Squares: {}".format(self.square_palindromes)
		print "Fair Squares: {}".format(self.fair_squares)


#functions
def parse_args(args):
	"""Open the input and output files"""
	if len(args) == 3:
		output_file_name = args[2]
	else:
		output_file_name = "FairAndSquare.out"
	
	try:
		input_file = open(args[1], 'r')
	except:
		print "Cannot open file {}".format(args[1])
		exit(1)
	
	try:
		output_file = open(output_file_name, 'w')
	except:
		input_file.close()
		print "Cannot open file {}".format(output_file_name)
		exit(1)
	
	return input_file, output_file

def parse_input(file_handle):
	"""Seperate lines into low/high numbers for cases"""
	cases = []
	data = file_handle.read().split('\n')[1:]
	# remove empty lines
	data = [x.split(' ') for x in data if x != '']
	data = [[int(x) for x in y] for y in data]
	[cases.append(case(data[x])) for x in range(len(data))]
	return cases

def write_results(cases, output_file):
	results = ["Case #{}: {}\n".format(x+1, len(cases[x].fair_squares)) for x in range(len(cases))]
	for result in results:
		output_file.write(result)
	output_file.close()
	
#procedure
input_file, output_file = parse_args(argv)
test_cases = parse_input(input_file)
[case.find_squares() for case in test_cases]
[case.find_palindromes() for case in test_cases]
[case.find_fair_squares() for case in test_cases]
write_results(test_cases, output_file)

#[x.print_info() for x in test_cases]