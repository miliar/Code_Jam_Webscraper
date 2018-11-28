#!/usr/bin/python

import sys

def read_input(filepath):
	f = open(filepath, 'r')
	cases = int(f.readline())
	for x in xrange(1, int(cases) + 1):
		solve_prob(x, [float(y) for y in f.readline().split()])

def solve_prob(case, list):
	C = list[0]
	F = list[1]
	X = list[2]

	per_second = 2.0
	spent_time = 0.0
	farm_build = 0.0
	current_time = (X / per_second) + 1
	min_time = X / per_second
	while (min_time < current_time):
		current_time = min_time
		farm_build += (C / per_second)
		per_second += F
		spent_time = farm_build + (X / per_second)
		if (spent_time < current_time):
			min_time = spent_time
		else:
			break

	print "Case #%d: %s" % (case, min_time)

def main():
	if (len(sys.argv) < 2):
		sys.exit("usage blablabla")

	read_input(sys.argv[1])

if __name__ == '__main__':
	main()