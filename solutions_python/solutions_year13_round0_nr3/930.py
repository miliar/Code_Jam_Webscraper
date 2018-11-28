#! /usr/bin/python
# -*- coding: utf-8 -*-


import logging
interact = False
logging.basicConfig(level=logging.INFO)
#logging.basicConfig(level=logging.DEBUG)
#interact = True

import math

## {{{ http://code.activestate.com/recipes/578231/ (r1)
def memodict(f):
    """ Memoization decorator for a function taking a single argument """
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret 
    return memodict().__getitem__
## end of http://code.activestate.com/recipes/578231/ }}}

@memodict
def square_is_palindrome(root):
	string = str(root**2)
	return string == string[::-1]

def make_palindrome(half, even):
	if even:
		return int(half + half[::-1])
	else:
		return int(half + half[:-1][::-1])
def increase_half(half, even):
	halflength = len(half)
	half = str(int(half)+1)
	if len(half) > halflength:
		if not even:
			half = half[:-1]
		even = not even
		logging.debug(("overflow to", half, even))
	return half, even

def solve_case(case):
	A, B = map(int, case.split(" "))
	logging.debug((A, B))
	solution = 0
	root_A = int(math.sqrt(A))
	str_root_A = str(root_A)
	length = len(str_root_A)
	half = str_root_A[:int((length+1)/2)]
	even = (length % 2) == 0
	root = make_palindrome(half, even)
	logging.debug(("preliminary", half, root, root**2))
	if root**2 < A:
		half, even = increase_half(half, even)
		root = make_palindrome(half, even)
		assert root**2 >= A
		logging.debug(("final", half, root, root**2))
	sqrt_B = math.sqrt(B)
	while root <= sqrt_B:
		logging.debug((half, even, root, square_is_palindrome(root)))
		if square_is_palindrome(root):
			solution += 1
		half, even = increase_half(half, even)
		root = make_palindrome(half, even)
	logging.debug(solution)
	return solution

def case_line(case_number, cases):
	"""case_number != list index"""
	if case_number % 100 == 0:
		logging.info(("solving", case_number))
	if interact:
		input()
	return "Case #{}: {}".format(case_number, solve_case(cases[case_number-1]))

def set_to_cases(set_):
	return set_.split("\n")[1:-1]

def set_to_cases_blocks(set_):
	return "\n".join(set_to_cases(set_)).split("\n\n")

def solve_set(set_):
	cases = set_to_cases(set_)
	return "\n".join(case_line(i+1, cases) for i in range(len(cases)))

test_in = """3
1 4
10 120
100 1000
"""

test_out = """Case #1: 2
Case #2: 0
Case #3: 2"""

def compare_test_case_line(case_number):
	test_solution_line = case_line(case_number, set_to_cases(test_in))
	test_out_line = test_out.split("\n")[case_number]
	if test_solution_line == test_out_line:
		logging.info("Test line {} passed".format(case_number))
	else:
		logging.warning("Test line {} failed".format(case_number))
		logging.info(test_solution_line)
		logging.info(test_out_line)


test_solution = solve_set(test_in)

if test_solution == test_out:
	logging.info("Test passed")
else:
	logging.warning("Test failed")
	logging.info(test_solution)
	logging.info(test_out)

problem_letter = "C"
attempt = 0

for problem_size in ("small", "large"):
	if input("Solve {} {}? (y)".format(problem_letter, problem_size)):
		name = "{}-{}{}-1".format(problem_letter, problem_size, problem_size == "small" and "-attempt{}".format(attempt) or "")
		with open(name + ".in") as file_in:
			with open(name + ".out".format(problem_letter, problem_size), "w") as file_out:
				print(solve_set(file_in.read()), file=file_out)

