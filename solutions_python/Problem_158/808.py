#!/usr/bin/python

import sys


def read_input(filename):
	cases = []

	with open(filename, 'r') as f:
		T = int(f.readline())
		for line in f:
			X, r, c = line.split()
			R = min(r, c)
			C = max(r, c)
			cases.append((int(X), int(R), int(C)))

	return cases


grids = [None, (1,1), (1,2), (2,2), (2,2), (2,3), (2,3)]

def process_case(case):
	X, R, C = case

	if X >= 7:
		return "RICHARD"
	if X == 1:
		return "GABRIEL"
	if X > R and X > C:
		return "RICHARD"
	if ((R * C) % X) != 0:
		return "RICHARD"
	if X == 2:
		return "GABRIEL"

	r, c = grids[X]
	if R < r or C < c:
		return "RICHARD"
	if X == 3:
		return "GABRIEL"
	if R == 2:
		return "RICHARD"
	else:
		return "GABRIEL"
			
	

if __name__ == '__main__':
	filename = sys.argv[1]
	cases = read_input(filename)
	for i, case in enumerate(cases):
		result = process_case(case)
		print "Case #{}: {}".format(i+1, result)
