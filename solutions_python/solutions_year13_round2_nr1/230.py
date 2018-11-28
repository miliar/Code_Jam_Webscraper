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
				logging.debug("Doing case #{}".format(case_num))
				answer = solver(case)
				logging.info("Solved case {}".format(case_num))
				write_case(fo, case_num, answer)

################################################################################

def read_case(f):
	a,n = read_ints(f)
	motes = read_ints(f)
	return ( a, motes )



def write_case(f, case_num, answer):
	output = "Case #{}: {}\n".format(case_num, answer) 
	logging.debug(output)
	f.write(output)

################################################################################

def solver(case):
	logging.debug(case)
	orig,motes = case
	
	# only remove if adding doesn't allow you to grow
	# only add motes of size current-1
	# if adding doesn't allow consumption; remove all the rest

	# while there are motes left, add one, if the number of ops for subproblem > number of motes, just delete all
	def solve(a, remaining, ops):
		# grow!
		grew=True
		while(grew and (len(remaining) > 0)):
			grew = False
			for pos,m in enumerate(remaining):
				if a>m:
					a+=m
					del remaining[pos]
					grew = True
					break

		# a is as big as it can get
		if len(remaining) == 0:
			return ops # ate everything
		else: # motes left
			# try growing until big enough to consume next
			smallest = min(remaining)
			grows = 0
			while (a <= smallest):
				a += a-1
				grows += 1
			testops = solve(a, remaining[:], 0) # copy list
			if (grows+testops) > len(remaining):
				# growing was slower than deleting - delete them all
				return ops + len(remaining)
			else:
				# growing was quicker than deleting remaining
				return ops + grows + testops

	if orig > 1:
		return solve(orig, motes[:], 0)
	else:
		return len(motes) # can't grow! delete them all

################################################################################

logging.basicConfig(format="%(message)s", level=logging.DEBUG)
solve(sys.argv[1])
