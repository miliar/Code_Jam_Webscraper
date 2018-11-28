#!/usr/bin/env python

import sys
import operator
from math import sqrt, floor, ceil

class InputFile:
	def __init__(self, fd):
		self.fd = fd
	def readInt(self):
		return int(self.fd.readline())
	def readIntegers(self):
		return tuple([int(x) for x in self.fd.readline().split()])
	def readString(self):
		return self.fd.readline()[:-1]

def cercaVittoria(a, b, c, d):
	xx = 0
	oo = 0
	tt = 0
	for x in (a, b, c, d):
		if x == "X": xx += 1
		if x == "O": oo += 1
		if x == "T": tt += 1
	
	if xx == 4: return "X won"
	if oo == 4: return "O won"
	if xx == 3 and tt == 1: return "X won"
	if oo == 3 and tt == 1: return "O won"
	return None

def solve(a):
	# CONTROLLA VITTORIA
	for k in range(4):
		r = cercaVittoria(a[k][0], a[k][1], a[k][2], a[k][3])
		if r is not None:
			return r
	
	for k in range(4):
		r = cercaVittoria(a[0][k], a[1][k], a[2][k], a[3][k])
		if r is not None:
			return r
	
	r = cercaVittoria(a[0][0], a[1][1], a[2][2], a[3][3])
	if r is not None:
		return r
	
	r = cercaVittoria(a[3][0], a[2][1], a[1][2], a[0][3])
	if r is not None:
		return r
	
	# CONTROLLA LIBERE
	libere = 0
	for x in range(4):
		for y in range(4):
			if a[x][y] == '.':
				libere += 1
	if libere > 0:
		return "Game has not completed"
	
	return "Draw"

inputfile = InputFile(sys.stdin)
T = inputfile.readInt()
for n in range(1,T+1):
	if n > 1: inputfile.readString()
	
	a = []
	a.append( inputfile.readString() )
	a.append( inputfile.readString() )
	a.append( inputfile.readString() )
	a.append( inputfile.readString() )
	
	result = solve(a)
	print "Case #%d: %s" % (n, result)

