import sys
import pprint


def solve_case(case_values):
	first_row = case_values[0][0]
	first_sorting = case_values[1:5]
	second_row = case_values[5][0]
	second_sorting = case_values[6:10]
	guess = set(first_sorting[first_row-1]) & set(second_sorting[second_row-1])
	if len(guess) == 1:
		return next(iter(guess))
	elif len(guess) > 1:
		return "Bad magician!"
	else:
		return "Volunteer cheated!"

data = [map(int, line.strip().split()) for line in sys.stdin.readlines()]

cases = data[0][0]
values = data[1:]

for case in range(cases):
	case_values = values[case*10:(case+1)*10]
	print "Case #%d: %s" % (case+1, solve_case(case_values))
	