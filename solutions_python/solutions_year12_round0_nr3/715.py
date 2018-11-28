#!/usr/bin/env python

import sys, os.path, re
import itertools, operator
#import pdb


def computeResult1(min, max):

	permutedSet = set()

	for nb in xrange(min, max+1):

		nbstr = str(nb)
		permutedStr = str(nb)
		# Try permutations
		for i in range(len(nbstr)):
			permutedStr = permutedStr[-1] + permutedStr[:-1]
			permutedNb = int(permutedStr)
			if min <= permutedNb <= max and permutedNb > nb:
				#print "%s %s" % (nb, permutedNb)
				permutedSet.add((nb, permutedNb))

	return len(permutedSet)

def computeResult2(min, max):
	
	result = 0	
	
	permutedSet = set()	
	for nb in xrange(min, max+1):
			
		permutedStr = str(nb)
		# Try permutations
		for i in range(len(permutedStr)):
			permutedStr = permutedStr[-1] + permutedStr[:-1]
			permutedNb = int(permutedStr)
			if nb < permutedNb <= max:
				permutedSet.add(permutedNb)
		result += len(permutedSet)
		permutedSet.clear()		

	return result

if __name__ == '__main__':

	if len(sys.argv) != 2 or not os.path.isfile(sys.argv[1]):
		inputFile = sys.stdin
	else:
		inputFile = open(sys.argv[1], 'r')

	testNB = 0

	for line in inputFile:

		# Skip first line
		if testNB == 0:
			testNB += 1
			continue


		min, max = [ int(x) for x in line.split() ]

		result = computeResult2(min, max)
		print("Case #%s: %s" % (testNB, result))
		testNB+=1

exit(0)