#!/usr/bin/env python

import fractions

def solve(line):
	N, PD, PG = map(int, line.strip().split())

	if (PG == 100 and PD != 100) or (PG == 0 and PD != 0):
		return "Broken"

	today = fractions.Fraction(PD,100)
	# find the win fraction

	if today.denominator > N:
		return "Broken"

	print N, "\t", PD, PG, "\t\t", today

	# D = c * today.denominator		where c is a positive integer
	# ever = fractions.Fraction(PG,100)
	# G = c * ever.denominator	

	# play basically infinite games more till ratio works out
	return "Possible"


def solveFile(Filename):
	inFile = open(Filename, "r")
	outFile = open(Filename[:-2]+"out", "w")
	tests = int(inFile.readline())
	for i, line in enumerate(inFile.readlines(),1):
		outFile.write("Case #{0}: {1}\n".format(i, solve(line)))

solveFile("example.in")
solveFile("A-small-attempt2.in")
solveFile("A-large.in")
