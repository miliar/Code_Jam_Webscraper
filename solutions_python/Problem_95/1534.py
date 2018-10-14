#!/usr/bin/env python

import string

def genMapping(lines):
	mapping = dict()

	inS = "aoe a zoo"
	inS += "ejp mysljylc kd kxveddknmc re jsicpdrysi"
	inS += "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
	inS += "de kr kd eoya kw aej tysr re ujdr lkgc jv"

	outS = "yeq y qee"
	outS += "our language is impossible to understand"
	outS += "there are twenty six factorial possibilities"
	outS += "so it is okay if you want to just give up"

	for i,o in zip(inS,outS):
		mapping[i] = o
		print "mapping ", o, "to", i

	mapping['q'] = 'z'

	print "in :", set(string.lowercase) - set(inS)
	print "out :", set(string.lowercase) - set(outS)

	return mapping


def solveFile(Filename):
	inFile = open(Filename, "r")
	outFile = open(Filename[:-2]+"out", "w")
	lines = inFile.readlines()[1:]

	mapping = genMapping(lines)

	for test, line in enumerate(lines):
		print "Case #{0} of file {1}".format(test + 1, Filename)
		outFile.write("Case #{0}: {1}\n".format(test + 1, ''.join(map(lambda x: mapping[x], line.strip()))))

solveFile("example.in")
solveFile("A-small-attempt0.in")
#solveFile("C-large-practice.in")
