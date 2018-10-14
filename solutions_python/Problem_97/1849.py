#!/usr/bin/env python

import math
import sys

def nextnumber(number, numDigits):
	word = str(number).zfill(numDigits)
	return int(word[1:] + word[0])

def numPairsForSingleNumber(number, min, max, numDigits):
	numPairs = 0
	candidate = nextnumber(number, numDigits)
	while candidate != number:
		if candidate >= min and candidate <= max and number < candidate:
			numPairs += 1
		candidate = nextnumber(candidate, numDigits)
	return numPairs

def numPairs(min, max):
	imin = int(min)
	imax = int(max)
	numDigits = len(max)
	num = 0;
	for i in range(imin,imax+1):
		num += numPairsForSingleNumber(i, imin, imax, numDigits)
	return num

i = 1
firstline = True
for line in sys.stdin:
	if firstline:
		firstline = False
	else:
		[min,max] = line.rstrip().split(' ')
		print 'Case #' + str(i) + ': ' + str(numPairs(min, max))
		i = i + 1

