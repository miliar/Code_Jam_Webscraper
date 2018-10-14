#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import division
import sys

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

def solve(c, f, x):
	base = 0
	vel = 2
	best = x/2

	while True:
		# A che punto lo compro
		base += c/vel
		# Aumenta velocità
		vel += f
		# Calcola quando raggiungerei x
		prox = base + x/vel

		if prox < best:
			best = prox
		else:
			return best;


inputfile = InputFile(sys.stdin)
T = inputfile.readInt()
for test in range(1,T+1):
	(c, f, x) = inputfile.readFloats()
	
	result = solve(c, f, x)
	
	print "Case #{test}: {result:.7f}".format(test=test, result=result)

