#! /usr/bin/python
# -*- coding: utf-8 -*-


import logging
#logging.basicConfig(level=logging.DEBUG)
#interact = True
interact = False

class Solved(Exception):
	pass
def mowed(line, mowed_perpendicular_lines, L, P):
	try:
		unmowed_fields = set(range(P))-set(mowed_perpendicular_lines)
		an_unmowed_field = list(unmowed_fields)[0]
		possible_height = line[an_unmowed_field]
		logging.debug(("unmowed", unmowed_fields, an_unmowed_field, mowed_perpendicular_lines))
	except IndexError:
		raise Solved
	return all((line[i] == possible_height) or ((line[i] < possible_height) and i in mowed_perpendicular_lines) for i in range(P))

def solve_case(case):
	logging.debug(("solving", case))
	N, M = case[0]
	grid = case[1:]
	mowed_rows = []
	mowed_columns = []
	try:
		while True:
			found_mowed = False
			for line, index, mowed_lines, mowed_perpendicular_lines, L, P, debug in [(grid[i], i, mowed_rows, mowed_columns, N, M, "rows") for i in range(N)] + [([grid[j][i] for j in range(N)], i, mowed_columns, mowed_rows, M, N, "columns") for i in range(M)]:
				logging.debug(("checking", debug, line, index, mowed_lines, mowed_perpendicular_lines))
				if index not in mowed_lines and mowed(line, mowed_perpendicular_lines, L, P):
					mowed_lines.append(index)
					found_mowed = True
					logging.debug("yes")
			if len(mowed_rows) == N or len(mowed_columns) == M:
				raise Solved
			if not found_mowed:
				logging.debug("NO")
				return "NO"
	except Solved:
		logging.debug("YES")
		return "YES"

def case_line(case_number, cases):
	"""case_number != list index"""
	if interact:
		input(case_number)
	return "Case #{}: {}".format(case_number, solve_case(cases[case_number-1]))

def set_to_cases(set_):
	return set_.split("\n")[1:-1]

def set_to_cases_blocks(set_):
	return "\n".join(set_to_cases(set_)).split("\n\n")

def set_to_cases_blocks_numbered(set_):
	it = iter(set_to_cases(set_))
	while True:
		try:
			N, M = map(int, next(it).split(" "))
		except StopIteration:
			break
		else:
			case = [(N, M)]
			for i in range(N):
				case.append(next(it).split(" "))
			yield case

def solve_set(set_):
	cases = list(set_to_cases_blocks_numbered(set_))
	return "\n".join(case_line(i+1, cases) for i in range(len(cases)))

test_in = """3
3 3
2 1 2
1 1 1
2 1 2
5 5
2 2 2 2 2
2 1 1 1 2
2 1 2 1 2
2 1 1 1 2
2 2 2 2 2
1 3
1 2 1
3 1
1
2
1
"""

test_out = """Case #1: YES
Case #2: NO
Case #3: YES
Case #4: YES"""

def compare_test_case_line(case_number):
	test_solution_line = case_line(case_number, set_to_cases(test_in))
	test_out_line = test_out.split("\n")[case_number]
	if test_solution_line == test_out_line:
		logging.info("Test line {} passed".format(case_number))
	else:
		logging.warning("Test line {} failed".format(case_number))
		logging.info(test_solution_line)
		logging.info(test_out_line)

logging.info(list(set_to_cases_blocks_numbered(test_in)))

test_solution = solve_set(test_in)

if test_solution == test_out:
	logging.info("Test passed")
else:
	logging.warning("Test failed")
	logging.info(test_solution)
	logging.info(test_out)

problem_letter = "B"
attempt = 1
for problem_size in ("small", "large"):
	if input("Solve {} {}? (y)".format(problem_letter, problem_size)):
		name = "{}-{}{}".format(problem_letter, problem_size, problem_size == "small" and "-attempt{}".format(attempt) or "")
		with open(name + ".in") as file_in:
			with open(name + ".out".format(problem_letter, problem_size), "w") as file_out:
				print(solve_set(file_in.read()), file=file_out)

