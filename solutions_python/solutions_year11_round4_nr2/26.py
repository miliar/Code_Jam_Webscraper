#!/usr/bin/env python

import collections
import heapq
import math

def solve(R, C, data):
	print R,C

	for k in xrange(min(R,C), 2, -1):
		halfK = (k-1)
		for r in xrange(0, R-(k-1)):
			for c in xrange(0, C-(k-1)):
				hmass = 0
				vmass = 0
				for i in xrange(k):
					for j in xrange(k):
						if (i in (0, k-1)) and (j in (0, k-1)):
							continue

						x = (2*i) - halfK
						y = (2*j) - halfK
						hmass += x * data[r+i][c+j]
						vmass += y * data[r+i][c+j]
#						print "\t", i,j, "\t", x,y, "\t", hmass, vmass

#				print k,r,c, "\t", hmass, vmass
				if hmass == 0 and vmass == 0:
					print "\t", k, r, c
					return k

	print "\tIMPOSSIBLE"
	return "IMPOSSIBLE"


def solveFile(Filename):
	inFile = open(Filename, "r")
	outFile = open(Filename[:-2]+"out", "w")
	tests = int(inFile.readline())
	for test in xrange(tests):
		R, C, D = map(int, inFile.readline().strip().split())
		data = [map(int, inFile.readline().strip()) for line in xrange(R)]

		outFile.write("Case #{0}: {1}\n".format(test+1, solve(R, C, data)))

solveFile("example.in")
solveFile("B-small-attempt0.in")
#solveFile("B-large.in")
