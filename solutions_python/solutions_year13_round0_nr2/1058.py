#!/usr/bin/python

#imports
from sys import argv, exit

#functions
def open_input(file_name):
	"""Open the input file and read, exit if file cannot be read."""
	try:
		input_file = open(file_name, 'r')
		input_data = input_file.read()
		input_file.close()
	except:
		print "Cannot open file {}.".format(file_name)
		exit(1)
	return input_data

def parse_input(input_data):
	"""Extract the number of test cases and the cases from the input file."""
	input_lines = input_data.split("\n")
	# remove any empty items from the list
	input_lines = [value for value in input_lines if value != '']
	num_of_cases = input_lines.pop(0)
	cases = []
	while len(input_lines) > 0:
		input_lines, case = get_cases(input_lines)
		cases.append(case)
	return cases

def get_cases(raw_cases):
	"""Return cases as a nested array based on the row/col count"""
	rows_cols = raw_cases.pop(0)
	rows_cols = rows_cols.split(' ')
	rows_count = int(rows_cols[0])
	case, raw_cases = raw_cases[:rows_count], raw_cases[rows_count:]
	for i in range(len(case)):
		case[i] = case[i].split(' ')
	case = [[int(col) for col in row] for row in case]
	return raw_cases, case
	
def create_working(cases):
	"""Creates a nested list identical in lengths to the input cases
	where the heights are all 100"""
	return [[[100 for col in row] for row in case] for case in cases]

def cut_working_cases(working, cases):
	for case_no in range(len(cases)):
	# cut rows
		for row in range(len(cases[case_no])):
			working[case_no][row] = row_cut(working[case_no][row], cases[case_no][row])
	# cut cols
		working[case_no] = cut_columns(working[case_no], cases[case_no])

def row_cut(working_row, goal_row):
	"""Cuts the rows"""
	max_height = sorted(goal_row)[-1]
	working_row = [min(col, max_height) for col in working_row]
	return working_row

def cut_columns(working, goal):
	# flip the case sideways
	goal_columns = [list(col) for col in zip(*goal)]
	working_columns = [list(col) for col in zip(*working)]
	working_columns = zip(*working)
	working_columns = [list(column) for column in working_columns]
	for i in range(len(goal_columns)):
		working_columns[i] = row_cut(working_columns[i], goal_columns[i])
	return [list(col) for col in zip(*working_columns)]

def check_cases(working, goals):
	return [int(working[x] == goals[x]) for x in range(len(goals))]

def process_results(results):
	yes_no = ["NO", "YES"]
	return ["Case #{}: {}".format(x + 1, yes_no[results[x]]) for x in range(len(results))]

def save_output(output, output_file):
	try:
		of = open(output_file, 'w')
	except:
		print "Cannot save results to: {}".format(output_file)
		exit(1)
	for result in output:
		of.write("{}\n".format(result))
	of.close()
	exit(0)
#procedure
input_data = open_input(argv[1])
cases = parse_input(input_data)
# working_cases are the lawns that will be cut to match the input cases
working_cases = create_working(cases)
cut_working_cases(working_cases, cases)
# chekc if cases match
results = check_cases(working_cases, cases)
output = process_results(results)
if len(argv) == 3:
	output_file = argv[2]
else:
	output_file = 'Lawnmower.out'
save_output(output, output_file)
print output
print cases
print working_cases