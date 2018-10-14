#!/usr/bin/python3

import sys

def parse(d):
	rcs = []
	l = d.splitlines()

	for i in range(int(l[0])):
		sm, sc = l[i + 1].split(' ', 1)
		rcs.append([int(x) for x in sc])
	
	return rcs

def solve(rc):
	ccc = 0
	ccl = 0
	cca = 0

	while True:
		while ccl <= ccc and ccl < len(rc):
			ccc += rc[ccl]
			ccl += 1

		if ccc == sum(rc) + cca:
			break

		iccl = ccl
		while not rc[ccl] and ccl < len(rc):
			ccl += 1

		d = ccl - iccl + 1
		cca += d
		ccc += d

	return cca

for i, rc in enumerate(parse(sys.stdin.read())):
	print('Case #%d: %d' % ((i + 1), solve(rc)))
