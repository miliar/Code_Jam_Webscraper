#!/usr/bin/python

import sys


def read_input(filename):
	cases = []

	with open(filename, 'r') as f:
		T = int(f.readline())
		for line in f:
			Smax, audience = line.split()
			cases.append((int(Smax), audience))

	return cases


def process_case(case):
	Smax, audience = case
	total = 0
	extra = 0

	for k, n_str in enumerate(audience):
		n = int(n_str)
		if not n:
			continue
		if total < k:
			extra += (k - total)
			total += (k - total)
		total += n
		if total > Smax:
			break
	
	return extra
			
	

if __name__ == '__main__':
	filename = sys.argv[1]
	cases = read_input(filename)
	for i, case in enumerate(cases):
		extra = process_case(case)
		print "Case #{}: {}".format(i+1, extra)
