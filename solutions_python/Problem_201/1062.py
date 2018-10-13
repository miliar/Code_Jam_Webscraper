#!/usr/bin/env python

from math import log

def BathRoom(line):
	n, k = map(int, line.split())
	devided = 2 ** int(log(k, 2))
	position = k - 2**int(log(k, 2))

	leftover = n - 2 ** int(log(k, 2)) + 1
	LandR = leftover//devided  + (position < leftover%devided) - 1

	return "{} {}".format(LandR//2 + LandR%2, LandR//2)

fileOut = open('file.out.txt', 'w')

with open('file.in.txt', 'r') as fileIn:
	for i in xrange(int(fileIn.readline())):
		fileOut.write('Case #{}: {}\n'.format(i + 1, BathRoom(fileIn.readline().strip())))

fileIn.close()
fileOut.close()
