#!/usr/bin/env python

import collections

def solve(line):
	items = (line.strip()).split()
	C = int(items[0])

	combineDict = {}
	for syms in items[1:C+1]:
		combineDict[syms[:2]] = syms[2]

	D = int(items[C+1])
	opposed = collections.defaultdict(list)
	for opposedPair in items[C+2:C+2+D]:
		opposed[opposedPair[0]].append(opposedPair[1])
		opposed[opposedPair[1]].append(opposedPair[0])

	elements = list(items[C+2+D+1])

	final = []
	last = ""
	for base in elements:
		combine = last + base
#		print combine, "\t", combine in combineDict, combine[::-1] in combineDict, combine in opposed, "\t", final
		if (combine in combineDict):
			last = combineDict[combine]
			final[-1] = last
		elif (combine[::-1] in combineDict):
			last = combineDict[combine[::-1]]
			final[-1] = last
		else:
			for opposingLetter in opposed[base]:
				if opposingLetter in final:
					last = ""
					final = []
					break
			else:
				last = base
				final.append(last)

	test = "[" + ', '.join(final) + "]"
#	print test
	return test

def solveFile(Filename):
	inFile = open(Filename, "r")
	outFile = open(Filename[:-2]+"out", "w")
	tests = int(inFile.readline())
	for i, line in enumerate(inFile.readlines(),1):
		outFile.write("Case #{0}: {1}\n".format(i, solve(line)))

solveFile("example.in")
solveFile("B-small-attempt0.in")
solveFile("B-large.in")
