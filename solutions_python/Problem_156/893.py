#!/usr/bin/python

import sys

def solvePancakes(pancakes, s, worst):
	pancakes.sort()
	m = pancakes[-1]
	score = s+m
	if s>worst:
		return score

	for d in range(2, m-1):
		# split the largest plate into d pieces
		splitLargest = [m/d]*(d-m%d) + [m/d+1]*(m%d)
		# s is the total number of special minutes so far. Cost for this tick is the number of cuts we made (d-1)
		r = solvePancakes(pancakes[:-1] + splitLargest, s+d-1, worst)
		score = min(score, r)

	return score

def main():
	f = open("input.txt")
	numTests = int(f.readline())
	output = ""
	failed = False
	for i in range(numTests):
		nonEmptyDiners = f.readline()
		pancakes = f.readline().split(' ')
		nonEmptyDiners = int(nonEmptyDiners)
		pancakes = [int(p) for p in pancakes]

		answer = solvePancakes(pancakes, 0, max(pancakes))
		if answer != None:
			output += "Case #%d: %d\n" % (i+1, answer)
			#print "Case #%d: %d" % (i+1, answer)
		else:
			output += "Case #%d: NOT POSSIBLE\n" % i+1
	fout = open("output.txt", "w")
	fout.write(output)

if __name__ == "__main__":
    main()

