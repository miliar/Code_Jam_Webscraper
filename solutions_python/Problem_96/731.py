#!/usr/bin/env python

import sys, os.path, re
import itertools, operator
import pdb


def computeResult(googlers_nb, surpr_nb, pBestResult, totalResults):

	# Sort results to get best 1st
	totalResults.sort(reverse=True)

	# Build potential scrores wo surprise event
	resultTriplets = []

	for res in totalResults:
		average = res / 3
		#mod = res % 3
		#triplet = [average if x+mod<3 else average+1 for x in range(3)]
		triplet = [average]*3
		for i in range(res %3):
			triplet[2-i]+=1

		resultTriplets.append(triplet)

	firstNonPassing = googlers_nb

	# Identify how many have already at least p
	for i in range(len(resultTriplets)):
		bestScore = resultTriplets[i][-1]
		if bestScore < pBestResult:
			firstNonPassing = i
			break

	passingGooglers = firstNonPassing

	# Now try to cheat a bit with surprises to raise best values (corrupted judges ?) and lower another one
	for i in range(firstNonPassing, len(resultTriplets)):
		if surpr_nb <= 0:
			break
		if resultTriplets[i][-1] + 1 >= pBestResult and resultTriplets[i][1] == resultTriplets[i][-1] and resultTriplets[i][1] > 0 :
			# That one could win as well, e.g 667 cannot be converted to 658; 000 cannot be converted to 0 -1 1
			passingGooglers+=1
			surpr_nb-=1

	return passingGooglers


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


		lineValues = line.split()
		googlers_nb, surpr_nb, pBestResult = [int(x) for x in lineValues[:3]]
		totalResults = [int(x) for x in lineValues[3:]]

		result = computeResult(googlers_nb, surpr_nb, pBestResult, totalResults)
		print("Case #%s: %s" % (testNB, result))
		testNB+=1

exit(0)