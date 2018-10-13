#! /usr/bin/python
# -*- coding: utf-8 -*-


import logging
logging.basicConfig(level=logging.DEBUG)

def search_winner(line):
	for values in ("XT", "OT"):
		if all(char in values for char in line):
			return values[0]

def solve_case(case):
	grid = case.split("\n")
	for line in [grid[i] for i in range(4)] + [[grid[j][i] for j in range(4)] for i in range(4)] + [[grid[i][i] for i in range(4)]] + [[grid[i][3-i] for i in range(4)]]:
		winner = search_winner(line)
		if winner:
			return winner + " won"
	else:
		if "." in case:
			return "Game has not completed"
		else:
			return "Draw"

def case_line(case_number, cases):
	"""case_number != list index"""
	return "Case #{}: {}".format(case_number, solve_case(cases[case_number-1]))

def set_to_cases(set_):
	return set_.split("\n")[1:-1]

def set_to_cases_blocks(set_):
	return "\n".join(set_to_cases(set_)).split("\n\n")

def solve_set(set_):
	cases = set_to_cases_blocks(set_)
	return "\n".join(case_line(i+1, cases) for i in range(len(cases)))

test_in = """6
XXXT
....
OO..
....

XOXT
XXOO
OXOX
XXOO

XOX.
OX..
....
....

OOXX
OXXX
OX.T
O..O

XXXO
..O.
.O..
T...

OXXX
XO..
..O.
...O
"""

test_out = """Case #1: X won
Case #2: Draw
Case #3: Game has not completed
Case #4: O won
Case #5: O won
Case #6: O won"""

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

problem_letter = "A"
attempt = 0

for problem_size in ("small", "large"):
	if input("Solve {} {}? (y)".format(problem_letter, problem_size)):
		name = "{}-{}".format(problem_letter, problem_size, attempt)
		with open(name + ".in") as file_in:
			with open(name + ".out".format(problem_letter, problem_size), "w") as file_out:
				print(solve_set(file_in.read()), file=file_out)

