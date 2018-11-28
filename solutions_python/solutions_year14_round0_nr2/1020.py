#!/usr/bin/env python
# Run file like so:
# 	python filename.py input.in

import sys

def main(args):

	# File to read
	input_file = "B-large.in"
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
	line = f_in.readline().strip().split(None)
	C = float(line[0])
	F = float(line[1])
	X = float(line[2])

	# DEBUG
	# print C
	# print F
	# print X

	# Set farms to 0
	upkeep = 0.0
	rate = 2.0
	time = X / rate
	# print time

	# Compare if current time is less than number of farms + 1
	while True:
		if (upkeep + (C / rate) + X / (rate + F)) < time:
			time = upkeep + (C / rate) + X / (rate + F)
			upkeep += (C / rate)
			rate += F
		else:
			break

		# DEBUG
		# print "upkeep: %f, rate: %f, time %f" % (upkeep, rate, time)

	return time


# Print result in the specific case format
def printResult(f_out, case_no, result):
	f_out.write("Case #%d:" % case_no)

	# SPECIFIC PRINT FORMAT HERE
	f_out.write(" %.7f" % result)

	f_out.write("\n")

if __name__ == '__main__':
	main(sys.argv[1:])