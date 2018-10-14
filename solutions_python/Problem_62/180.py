#!/usr/bin/python

import sys
import re

testIn = open(sys.argv[1], "r")
testOut = open(sys.argv[2], "w")
nbTests = int(testIn.readline())


for nbTest in range(1,nbTests+1):
	line = testIn.readline()[:-1]
	line = line.split(" ")
	N = int(line[0])

	ropes = []
	line = testIn.readline()[:-1].split(" ")
	ropes.append([int(line[0]), int(line[1])])

	counter = 0
	for i in xrange(N-1):
		values = testIn.readline()[:-1].split(" ")
		A,B = int(values[0]), int(values[1])
		for wire in ropes:
			if A<wire[0] and B>wire[1]:
				counter += 1
			elif A>wire[0] and B<wire[1]:
				counter += 1
		ropes.append([A,B])

	outLine = "Case #"+str(nbTest)+": "+str(counter)
	print outLine
	testOut.write(outLine+"\n")

testIn.close()
testOut.close()
