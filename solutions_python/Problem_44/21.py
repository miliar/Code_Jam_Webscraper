#!/usr/bin/env python2.6
from __future__ import division
import math
import sys

def calc(fireflyLines):
	rslt = []
	for i in range(6):
		rslt.append(0)
	count = 0
	for firefly in fireflyLines:
		words = firefly.split(" ")
		for i in range(6):
			rslt[i] += int(words[i])
		count += 1
	for i in range(6):
		rslt[i] /= count
	return findDistance(rslt)

def findDistance(coords):
	min = 0
	max = 123456789
	while max - min > 1e-8:
		new = (max + min) / 2
		if dist(coords, max) >= dist(coords, min):
			max = new
		else:
			min = new
	if max > 123456788:
		print "WARNING: minimum not found. Try setting a higher value for max."
		sys.exit(1)
	t = (max + min) / 2
	d = dist(coords, t)
	return (d, t)

def dist(coords, time):
	x = coords[0] + coords[3] * time
	y = coords[1] + coords[4] * time
	z = coords[2] + coords[5] * time
	return math.sqrt(x**2 + y**2 + z**2)

lines = sys.stdin.read().split("\n")
numTestCases = int(lines[0])
lines = lines[1:]
linenr = 0
for testCase in range(numTestCases):
	numLines = int(lines[linenr])
	fireflyLines = lines[linenr+1:linenr+1+numLines]
	linenr += numLines + 1
	dt = calc(fireflyLines)
	print "Case #%d: %.8f %.8f" % (testCase + 1, dt[0], dt[1])
