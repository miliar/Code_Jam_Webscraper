import sys
import itertools
import math
import logging
from functools import partial

# CodeJam I/O helpers adapted from royf

# A single word (minus whitespace)
def read_word(f):
	return next(f).strip()

# A single int (given base)
def read_int(f, base=10):
	return int(read_word(f), base)

# A list of characters (including whitespace)
def read_letters(f):
	return list(read_word(f))

# A list of digits (whitespace results in error)
def read_digits(f, base=10):
	return [int(x, base) for x in read_letters(f)]

# A list of words split by whitespace
def read_words(f, delimiter=' '):
	return read_word(f).split(delimiter)

# A list of values interpreted by converter, split by delimiter
def read_values(f, converter, delimiter=' '):
	return [converter(x) for x in read_words(f, delimiter)]

# A list of ints split by whitespace
def read_ints(f, base=10, delimiter=' '):
	return read_values(f, partial(int,base=base), delimiter)

# Read 'length' lines, return a list interpreting each line using 'reader=read_ints'
# Use functools.partial to specify reader arguments
def read_arr(f, length, reader=read_ints):
	res = []
	for _i in range(length):
		res.append(reader(f))
	return res

def solve(fn, out_fn=None):
	in_fn = fn + '.in'
	if out_fn is None:
		out_fn = fn + '.out'
	with open(in_fn, 'r') as fi:
		with open(out_fn, 'w') as fo:
			T = read_int(fi)
			for case_num in range(1, T+1):
				case = read_case(fi)
				answer = solver(case)
				logging.info("Solved case {}".format(case_num))
				write_case(fo, case_num, answer)

################################################################################

def read_case(f):
	return read_ints(f)



def write_case(f, case_num, answer):
	output = "Case #{}: {}\n".format(case_num, answer) 
	logging.debug(output)
	f.write(output)

################################################################################

def solver(case):
	def is_palindrome(i):
		s = str(i)
		for i in range(0,len(s)/2):
			if s[i] != s[-1 - i]:
				return False
		return True
	logging.debug(case)

	lower_squares =  int(math.ceil(math.sqrt(case[0])))
	upper_squares =  int(math.floor(math.sqrt(case[-1])))
	count = 0
	for root in range(lower_squares,upper_squares+1):
		if is_palindrome(root):
			square = root*root
			if is_palindrome(square):
				logging.debug(square)
				count+=1

	return count

################################################################################

logging.basicConfig(format="%(message)s", level=logging.DEBUG)
solve(sys.argv[1])
