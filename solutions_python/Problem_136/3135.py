"""
Alon Daks
CodeJam 2014, Qualification Round
Student at UC Berkeley (Class of 2016)
"""

import sys

class CookieClicker(object):
	def __init__(self, puzzle_input):
		self.puzzle_input = puzzle_input
		self.case_num = 0

	def solve_puzzles(self):
		while self.case_num < int(self.puzzle_input.num_cases):
			self.solve_next_case()

	def solve_next_case(self):
		case_line = self.puzzle_input.lines[self.case_num]
		case_line = [float(x) for x in case_line.split(' ')]
		c, f, x = case_line[0], case_line[1], case_line[2]
		min_seconds = find_min_seconds(c, f, x)
		self.case_num += 1
		print "Case #{0}: {1}".format(self.case_num, min_seconds)

class CodeJamIO(object):
	def __init__(self, input_file):
		self.lines = open(input_file).readlines()
		self.num_cases = self.lines.pop(0)

""" 
Helper Functions
"""

def find_min_seconds(cost, rate_increase, goal):
	total_elapsed_time = 0
	cookie_rate = 2
	while goal/cookie_rate > cost/cookie_rate + goal/(cookie_rate+rate_increase):
		total_elapsed_time += cost/cookie_rate
		cookie_rate += rate_increase
	return round(goal/cookie_rate + total_elapsed_time, 7)


if __name__ == '__main__':
	puzzle_input = CodeJamIO(sys.argv[1])
	cookie_puzzle = CookieClicker(puzzle_input)
	cookie_puzzle.solve_puzzles()