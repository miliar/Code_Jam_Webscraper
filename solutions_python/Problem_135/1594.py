#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import division
import sys
from sets import Set

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
	def readString(self):
		return self.fd.readline()[:-1]

def solve(a, asquare, b, bsquare):
	primo = Set(asquare[a-1])
	secondo = Set(bsquare[b-1])

	possibili = primo.intersection(secondo)

	if len(possibili) == 1:
		return possibili.pop()
	else:
		if len(possibili) > 1:
			return "Bad magician!" # 2+ possibilità
		else:
			return "Volunteer cheated!" # Impossibile


inputfile = InputFile(sys.stdin)
T = inputfile.readInt()
for test in range(1,T+1):
	
	a = inputfile.readInt()
	asquare = []
	for i in range(4):
		asquare.append(inputfile.readIntegersList())
	
	b = inputfile.readInt()
	bsquare = []
	for i in range(4):
		bsquare.append(inputfile.readIntegersList())
	
	result = solve(a, asquare, b, bsquare)
	
	print "Case #{test}: {result}".format(test=test, result=result)

