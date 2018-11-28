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
	N = list(line[0])

	# DEBUG
	#print len(N)

	for i in range(len(N) - 1):
		N = adjustNum(N, i)

	# Convert to num
	output = int(''.join(N))

	return str(output)

def adjustNum(N, idx):
	if int(N[idx]) > int(N[idx+1]):
		N[idx] = str(int(N[idx]) - 1)

		for nxt in range(idx + 1, len(N)):
			N[nxt] = str(9)

		if idx > 0:
			return adjustNum(N, idx - 1)

	return N

# Print result in the specific case format
def printResult(f_out, case_no, result):
	f_out.write("Case #%d: " % case_no)

	# SPECIFIC PRINT FORMAT HERE
	f_out.write("%s" % result)

	f_out.write("\n")

if __name__ == '__main__':
	main(sys.argv[1:])
