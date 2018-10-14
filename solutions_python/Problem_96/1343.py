#!/usr/bin/env python

def solveFile(Filename):
	inFile = open(Filename, "r")
	outFile = open(Filename[:-2]+"out", "w")

	count = inFile.readline()
	lines = [map(int,line.split()) for line in inFile.readlines()]

	for test, line in enumerate(lines):
		print "Case #{0} of file {1}".format(test + 1, Filename)

		N, S, p = line[0], line[1], line[2]	
		normalPoint = p + 2 * max(p-1,0)
		specialPoint = p + 2 * max(p-2,0)
		count = special = 0
		for i in line[3:]:
			if i >= normalPoint:
				count += 1
			elif i >= specialPoint:
				special += 1

		outFile.write("Case #{0}: {1}\n".format(test + 1, count + min(special, S)))

solveFile("example.in")
solveFile("B-small-attempt0.in")
solveFile("B-large.in")
