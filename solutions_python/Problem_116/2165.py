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
				logging.debug(case)
				answer = solver(case)
				logging.info("Solved case {}".format(case_num))
				write_case(fo, case_num, answer)

################################################################################

def read_case(f):
	rows = []
	for rownum in range(4):
		rows += [read_letters(f)]
	try:
		read_word(f) # discard blank line
	except:
		None
	return(rows)



def write_case(f, case_num, answer):
	f.write("Case #{}: {}\n".format(case_num, answer))
	logging.debug("Case #{}: {}\n".format(case_num, answer))

################################################################################

def solver(case):
	def wins(row):
		def comp(a,b):
			if a == None:
				return None
			if a == '.':
				return None
			if a == 'T':
				return b
			if (a == b) or (b=='T'): # They're both X or O, or there's a T
				return a
			return None

		return reduce(comp, row)

	def checkrows(rows):
		for row in rows:
			result = wins(list(row))
			if result:
				return result + " won"
		return None
	
	# Check rows
	result = checkrows(case)
	if result:
		return result

	# Check columns
	transposed = zip(*case)
	logging.debug(transposed) # tuples not list
	result = checkrows(transposed)
	if result:
		return result

	# top left to bottom right diag
	result = wins([case[i][i] for i in range(4)])
	if result:
		return result + " won"

	# bottom left to top right diag
	result = wins([case[3-i][i] for i in range(4)])
	if result:
		return result + " won"


	# no-one has won
	for row in case:
		if '.' in row:
			return 'Game has not completed'
	return 'Draw'

################################################################################

logging.basicConfig(format="%(message)s", level=logging.INFO)
solve(sys.argv[1])
