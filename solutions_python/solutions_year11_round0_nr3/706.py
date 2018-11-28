#!/usr/bin/env python

import sys

def powerset(seq):
	if len(seq) <= 1:
		yield seq
		yield []
	else:
		for item in powerset(seq[1:]):
			yield [seq[0]]+item
			yield item


def xorsum(x1):
	sum = 0
	for i in x1:
		sum = sum ^ i
	return sum

def goodsum(x1):
	sum = 0
	for i in x1:
		sum = sum + i
	return sum

def solve(c):
	words = c.split()
	ints = [int(w) for w in words]
	ints.sort()
	ints.reverse()

	best = 0
	cando = False;
	for s in powerset(range(len(ints))):
		x1 = []
		x2 = []

		if len(s) == len(ints):
			continue

		if len(s) == 0:
			continue

		for i in range(len(ints)):
			if i in s:
				x1.append(ints[i])
			else:
				x2.append(ints[i])

		badsum1 = xorsum(x1)
		badsum2 = xorsum(x2)

		if badsum1 == badsum2:
			cando = True
			d =  max(goodsum(x1), goodsum(x2))
			if best < d:
				best = d

	return cando, best

if __name__ == '__main__':
	lines = open(sys.argv[1]).readlines()
	tests = int(lines[0].strip())
	index = 1
	c = 1
	for i in range(tests):
		tc = lines[index+1].strip()
		index += 2

		cando, best = solve(tc)
		if cando:
			print 'Case #%d: %d' % (c, best)
		else:
			print 'Case #%d: NO' % c
		c = c + 1
