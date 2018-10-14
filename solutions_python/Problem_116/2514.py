#!/usr/bin/env python
import sys

try:
	input_f_name = sys.argv[1]
except:
	print "Provide a file name."
	sys.exit(1)

f = file(input_f_name, 'r')
inp = [ x for x in f.read().split('\n') ][:-1]
num_cases = int(inp.pop(0))
input_lines_per_case = (len(inp) / num_cases)-1

def test_combination(comb):
	if "T" in comb:
		comb.remove("T")
	for symbol in ["X", "O"]:
		if comb.count(symbol) == len(comb):
			return symbol
	return False

def solve_case(case_input):
	board = [ [ c for c in row_string ] for row_string in case_input ]
	combinations = []
	for row in board:
		combinations.append(row)
	for i in range(4):
		column = [ row[i] for row in board ]
		combinations.append(column)
	for diag_def in [ [[0,0], [1,1], [2,2], [3,3]] , [[0,3], [1,2], [2,1], [3,0]] ]:
		diagonal = [ board[coord[0]][coord[1]] for coord in diag_def ]
		combinations.append(diagonal)
	for combination in combinations:
		res = test_combination(combination)
		if res:
			return "%s won" % res
	for row in board:
		if "." in row:
			return "Game has not completed"
	return "Draw"

for i_case in range(num_cases):
	input_range_start = (i_case * input_lines_per_case) + i_case
	output = solve_case(inp[ input_range_start : input_range_start + input_lines_per_case ])
	print "Case #%d: %s" % (i_case+1, output)
