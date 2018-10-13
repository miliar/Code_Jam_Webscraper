#!C:/Python/python.exe -u
# -*- coding: utf-8 -*-

import sys
import string

outStr = "Case #{}: {}"
file = open(sys.argv[1], 'r')

numberOfCases = int(file.readline().strip())

for i in xrange(numberOfCases):
	fPos = int(file.readline().strip())
	fSet = []
	for n in xrange(4):
		fSet.append( [ int(x) for x in file.readline().split() ] )
	sPos = int(file.readline().strip())
	sSet = []
	for n in xrange(4):
		sSet.append( [int(x) for x in file.readline().split() ] )

	result = []
	
	for number in fSet[fPos-1]:
		for seNumber in sSet[sPos-1]:
			if number == seNumber:
				result.append(number)

	if len(result) == 0:
		print outStr.format(i+1, "Volunteer cheated!" )
	elif len(result) == 1:
		print outStr.format(i+1, result[0] )
	else:
		print outStr.format(i+1, "Bad magician!" )

file.close()
