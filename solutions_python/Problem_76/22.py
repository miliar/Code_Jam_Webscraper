#!/usr/bin/env python

import itertools

def xor(x,y):
	return x^y

def solve(line):
	values = list(map(int, (line.strip()).split()))

	if reduce(xor, values) != 0:
		return "NO"

	smallest = min(values)
	values.remove(smallest)
	return sum(values)

def solveFile(Filename):
	inFile = open(Filename, "r")
	outFile = open(Filename[:-2]+"out", "w")
	tests = int(inFile.readline())
	for i, line in enumerate(inFile.readlines()[1::2],1):
		outFile.write("Case #{0}: {1}\n".format(i, solve(line)))

#solveFile("example.in")
#solveFile("C-small-attempt0.in")
solveFile("C-large.in")

