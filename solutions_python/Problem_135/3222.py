"""
Alon Daks
CodeJam 2014, Qualification Round
Student at UC Berkeley (Class of 2016)
"""

import sys

class MagicTrick(object):
	def __init__(self, puzzle_input):
		self.puzzle_input = puzzle_input
		self.case_num = 0

	def solve_next_case(self):
		first_arrangment = self.puzzle_input.lines[self.case_num*10:self.case_num*10+5]
		second_arrangment = self.puzzle_input.lines[self.case_num*10+5:self.case_num*10+10]
		intersection = find_intersection(first_arrangment, second_arrangment)
		self.case_num += 1
		if len(intersection) > 1:
			print "Case #{0}: {1}".format(self.case_num,"Bad magician!") 
		elif len(intersection) == 0:
			print "Case #{0}: {1}".format(self.case_num,"Volunteer cheated!") 
		else: 
			print "Case #{0}: {1}".format(self.case_num,[x for x in intersection][0])

	def solve_puzzles(self):
		while self.case_num < int(self.puzzle_input.num_cases):
			self.solve_next_case()

class CodeJamIO(object):
	def __init__(self, input_file):
		self.lines = open(input_file).readlines()
		self.num_cases = self.lines.pop(0)

"""
Helper Functions
"""
def find_intersection(first_arrangment, second_arrangment): 
		first_arrangment_row = int(first_arrangment[0])
		second_arrangment_row = int(second_arrangment[0])
		first_set = {int(x) for x in first_arrangment[first_arrangment_row].split(' ')}
		second_set = {int(x) for x in second_arrangment[second_arrangment_row].split(' ')}
		return first_set.intersection(second_set)

	
if __name__ == '__main__':
	puzzle_input = CodeJamIO(sys.argv[1])
	magic_trick = MagicTrick(puzzle_input)
	magic_trick.solve_puzzles()