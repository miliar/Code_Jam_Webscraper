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

def reverseNumber(n):
	partial = 0
	while n > 0:
		partial *= 10
		partial += n % 10
		n = n/10
	return partial

def reverseNumberB(n):
	s = str(n)
	return int(s[::-1])

def isPalindrome(n):
	return n == reverseNumber(n)
	
def solve(a, b):
	trovati = 0
	for x in range(int(ceil(sqrt(a))), int(floor(sqrt(b)))+1):
		if isPalindrome(x) and isPalindrome(x*x):
			trovati += 1
	
	return trovati

inputfile = InputFile(sys.stdin)
T = inputfile.readInt()
for n in range(1,T+1):
	(a, b) = inputfile.readIntegers()
	result = solve(a, b)
	print "Case #%d: %d" % (n, result)

