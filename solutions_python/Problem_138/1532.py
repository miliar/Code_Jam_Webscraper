#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import division
import sys
from sets import Set
from collections import Counter

class InputFile:
	def __init__(self, fd):
		self.fd = fd
	def readInt(self):
		return int(self.fd.readline())
	def readIntegers(self):
		return tuple([int(x) for x in self.fd.readline().split()])
	def readFloats(self):
		return tuple([float(x) for x in self.fd.readline().split()])
	def readIntegersList(self):
		return [int(x) for x in self.fd.readline().split()]
	def readFloatsList(self):
		return [float(x) for x in self.fd.readline().split()]
	def readString(self):
		return self.fd.readline()[:-1]

def solve(n, naomi, ken):
	values = []
	for w in naomi:
		values.append((w, 'naomi'))
	for w in ken:
		values.append((w, 'ken'))
	values.sort()

	counter_naomi = 0
	for (w, owner) in values:
		if owner == 'ken':
			if counter_naomi > 0:
				counter_naomi -= 1
		else:
			counter_naomi += 1
	war_points = counter_naomi
	
	values.reverse()
	deceitful_points = 0
	counter_naomi = 0
	for (w, owner) in values:
		if owner == 'ken':
			if counter_naomi > 0:
				deceitful_points += 1
				counter_naomi -= 1
		else:
			counter_naomi += 1

	if deceitful_points < war_points:
		print "ATTENZIONE", deceitful_points, war_points

	return (deceitful_points, war_points)

inputfile = InputFile(sys.stdin)
T = inputfile.readInt()
for test in range(1,T+1):
	
	n = inputfile.readInt()
	naomi = inputfile.readFloatsList()
	ken = inputfile.readFloatsList()
	
	(deceitful, war) = solve(n, naomi, ken)
	
	print "Case #{test}: {deceitful} {war}".format(test=test, deceitful=deceitful, war=war)

