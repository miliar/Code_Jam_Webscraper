#!/usr/bin/env python
# Run file like so:
# 	python filename.py input.in

import sys

def main(args):

	# File to read
	input_file = "A-small-attempt0.in"
	if (len(args) > 0):
		input_file = args[0].strip()

	# Open files
	f_in = open(input_file, 'r')
	f_out = open('output.txt', 'w')

	# Get number of cases
	cases = int(f_in.readline().strip())

	# Print all cases
	for i in range(1, cases+1):
		result = doCase(f_in)
		
		if not result:
			print "Error"
			sys.exit(0)

		printResult(f_out, i, result)


def doCase(f_in):
	# Default no match
	result = "Volunteer cheated!"

	row_1 = int(f_in.readline().strip())
	shuffle_1 = []

	for i in range(4):
		if i == row_1 - 1:
			shuffle_1 = f_in.readline().strip().split(None)
		else:
			f_in.readline().strip()

	row_2 = int(f_in.readline().strip())
	shuffle_2 = []

	for i in range(4):
		if i == row_2 - 1:
			shuffle_2 = f_in.readline().strip().split(None)
		else:
			f_in.readline().strip()

	# DEBUG
	# print shuffle_1
	# print shuffle_2

	for i in range(len(shuffle_1)):
		for j in range(len(shuffle_2)):
			if shuffle_1[i] == shuffle_2[j]:
				if result == "Volunteer cheated!":
					result = shuffle_1[i]
				else:
					return "Bad magician!"

	return result


# Print result in the specific case format
def printResult(f_out, case_no, result):
	f_out.write("Case #%d:" % case_no)

	# SPECIFIC PRINT FORMAT HERE
	f_out.write(" %s" % result)

	f_out.write("\n")

if __name__ == '__main__':
	main(sys.argv[1:])