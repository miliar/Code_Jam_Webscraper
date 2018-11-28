#!/usr/bin/env python
# Run file like so:
# 	python filename.py input.in

import sys

DEBUG = False

def main(args):

	# File to read
	input_file = "D-large.in"
	if (len(args) > 0):
		input_file = args[0].strip()

	# Open files
	f_in = open(input_file, 'r')
	f_out = open('output.txt', 'w')

	# Get number of cases
	cases = int(f_in.readline().strip())

	# Print all cases
	for i in range(1, cases+1):

		if DEBUG:
			print "Case %d:" % i

		result = doCase(f_in)
		
		if not result:
			print "Error"
			sys.exit(0)

		printResult(f_out, i, result)


def doCase(f_in):
	N = int(f_in.readline().strip())
	naomi = sorted([float(n) for n in f_in.readline().strip().split(None)])
	ken = sorted([float(n) for n in f_in.readline().strip().split(None)])

	if DEBUG:
		print naomi
		print ken

	d_points = war(N, ken, naomi, True)
	w_points = war(N, ken, naomi, False)

	#print "d: %d, w: %d" % (d_points, w_points)

	return [d_points, w_points]

def war(N, ken, naomi, deceit=False):
	left = N
	k = ken[:]
	n = naomi[:]
	points = 0

	# if naomi's lowest stone is higher than ken's lowest
	# play the highest stone first
	while left > 0:
		low_k = k[0]
		high_n = n[-1]

		if n[-1] > k[-1]:
			points += 1
			k.pop(0)
			if deceit:
				for i in range(len(n)):
					if (n[i] > low_k):
						n.pop(i)
						break
			else:
				n.pop()
		else:
			for i in range(len(k)):
				if k[i] > high_n:
					k.pop(i)
					break

			if deceit:
				n.pop(0)
			else:
				n.pop()

		left -= 1

	return points

# Print result in the specific case format
def printResult(f_out, case_no, result):
	f_out.write("Case #%d:" % case_no)

	# SPECIFIC PRINT FORMAT HERE
	for r in result:
		f_out.write(" %d" % r)

	f_out.write("\n")

if __name__ == '__main__':
	main(sys.argv[1:])