#!/usr/bin/env python
from collections import defaultdict
import sys
infile = sys.argv[1]
#outfile = sys.argv[2]

indata = open(infile, 'r').readlines()
#print indata

numcases = int(indata[0].strip())
cases = [x.strip().split(' ') for x in indata[1:]]

for j in range(0, numcases):
	case = cases[j]
	numcombines = int(case[0])
	combines = case[1:1+numcombines]
	combinedict = dict()
	for x in combines:
		combinedict[x[0]+x[1]] = x[2]
		combinedict[x[1]+x[0]] = x[2]
	numopposed = int(case[1+numcombines])
	opposeds = case[1+numcombines+1:1+numcombines+1+numopposed]
	opposeddict = defaultdict(set)
	for x in opposeds:
		opposeddict[x[0]].add(x[1])
		opposeddict[x[1]].add(x[0])
	toinvoke = case[-1]
	#print case
	#print combinedict
	#print opposeddict
	#print toinvoke

	#Solve
	elements = []
	for x in toinvoke:
		if len(elements) == 0:
			elements = [x]
		elif x+elements[-1] in combinedict:
			elements = elements[:-1] + [combinedict[x+elements[-1]]]
		elif len(set(elements).intersection(opposeddict[x])) != 0:
			elements = []
		else:
			elements += [x]

	if len(elements) == 0:
		output = '[]'
	else:
		output = '['
		for x in elements:
			output += x + ', '
		output = output[:-2] + ']'

	print "Case #" + str(j+1) + ": " + output
