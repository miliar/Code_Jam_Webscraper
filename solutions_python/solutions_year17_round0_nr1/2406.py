#!/usr/bin/env python
# Run file like so:
# 	python filename.py input.in

import sys

def main(args):

	# File to read
	input_file = "A-large.in"
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
	S = list(line[0])
	K = int(line[1])

	# DEBUG
	#print S, K

	count = 0

	while len(S) > 0:

		if S[0] == '+':
			S = S[1:]

		elif S[0] == '-' and len(S) >= K:
			S = flipPancake(S, K)
			count += 1

		else:
			return "IMPOSSIBLE"


	return str(count)

def flipPancake(S, K):
	for i in range(K):
		if S[i] == '+':
			S[i] = '-'

		else:
			S[i] = '+'

	return S

# Print result in the specific case format
def printResult(f_out, case_no, result):
	f_out.write("Case #%d: " % case_no)

	# SPECIFIC PRINT FORMAT HERE
	f_out.write("%s" % result)

	f_out.write("\n")

if __name__ == '__main__':
	main(sys.argv[1:])
