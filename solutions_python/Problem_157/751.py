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

def char2num(s):
	if s == "i":
		return 2
	elif s == "j":
		return 3
	elif s == "k":
		return 4
	else:
		assert(False)

def num2str(n):
	assert(n in [1,2,3,4,-1,-2,-3,-4])
	s = ""
	if n < 0:
		s += "-"
		n = -n
	s += ("1ijk")[n-1]
	return s

mat = [
	[ 1,  2,  3,  4],
	[ 2, -1,  4, -3],
	[ 3, -4, -1,  2],
	[ 4,  3, -2, -1]
]
def mult(a, b):
	assert(a in [1,2,3,4,-1,-2,-3,-4])
	assert(b in [1,2,3,4,-1,-2,-3,-4])
	sign = 1
	if a < 0:
		a = -a
		sign = -sign
	if b < 0:
		b = -b
		sign = -sign
	return sign * mat[a-1][b-1]

def power(a, b):
	""" a ^ b """
	b = b % 4
	res = 1
	for i in range(b):
		res = mult(res, a)
	return res

def inverse(a, b, c):
	"x such that a*x*b = c"
	for x in [1,2,3,4,-1,-2,-3,-4]:
		if mult(mult(a, x), b) == c:
			return x
	raise Exception("no inverse for {1} {2} {3}".format(a, b, c))

def multStr(s):
	res = 1
	for c in s:
		res = mult(res, char2num(c))
	return res

def initialize(s):
	global memPrefix, memSuffix, memWhole
	l = len(s)
	memPrefix = [0] * l
	memSuffix = [0] * l

	curr = 1
	for (i, c) in enumerate(s):
		curr = mult(curr, char2num(c))
		memPrefix[i] = curr
	memWhole = curr
	curr = 1
	for (i, c) in enumerate(s[::-1]):
		curr = mult(char2num(c), curr)
		memSuffix[l-1-i] = curr

def mulPrefixChars(n):
	""" s[:n] """
	if n == 0: return 1
	return memPrefix[n-1]

def mulSuffixChars(n):
	""" s[n:] """
	if n == len(memSuffix): return 1
	return memSuffix[n]

def mulAllChars():
	""" s[a:b] s.t. s[:a] * x * s[b:] = s """
	return memWhole

def mulInnerChars(a, b):
	""" s[a:b] s.t. s[:a] * x * s[b:] = s """
	return inverse(mulPrefixChars(a), mulSuffixChars(b), memWhole)

def validSingle(s, rep, a, b, x, y):
	""" s*a + s[:x] -- s[x:y] -- s[y:] + s*b """
	assert(a + b + 1 == rep)
	assert(x <= y)
	ii = mult(power(mulAllChars(), a), mulPrefixChars(x))
	#assert(ii == multStr(s*a + s[:x]))
	#jj = mulInnerChars(x, y)
	#assert(jj == multStr(s[x:y]))
	kk = mult(mulSuffixChars(y), power(mulAllChars(), b))
	#assert(kk == multStr(s[y:] + s*(b%4)))
	#if ii == 2 and kk == 4:
	#	assert(3 == mulInnerChars(x, y))
	return ii == 2 and kk == 4

def validDouble(s, rep, a, b, c, x, y):
	""" s*a + s[:x] -- s[x:] + s*b + s[:y] -- s[y:] + s*c """
	assert(a + b + c + 2 == rep)
	ii = mult(power(mulAllChars(), a), mulPrefixChars(x))
	#assert(ii == multStr(s*a + s[:x]))
	#jj = mult(mult(mulSuffixChars(x), power(mulAllChars(), b)), mulPrefixChars(y))
	#assert(jj == multStr(s[x:] + s*b + s[:y]))
	kk = mult(mulSuffixChars(y), power(mulAllChars(), c))
	#assert(kk == multStr(s[y:] + s*(c%4)))
	#if ii == 2 and kk == 4:
	#	assert(3 == mult(mult(mulSuffixChars(x), power(mulAllChars(), b)), mulPrefixChars(y)))
	return ii == 2 and kk == 4

def solve(s, rep):
	initialize(s)

	if power(mulAllChars(), rep) != -1:
		assert(-1 != multStr(s*(rep%4)))
		return False

	for a in [0,1,2,3,4]:
		b = rep - 1 - a
		if b < 0:
			continue
		for x in range(len(s)+1):
			for y in range(x+1, len(s)+1):
				if a == 0 and x == 0:
					continue
				if b == 0 and y == len(s):
					continue
				if validSingle(s, rep, a, b, x, y):
					#print "validSingle", a, b, x, y
					return True

	for a in [0,1,2,3,4]:
		for b in [0,1,2,3,4]:
			c = rep - 2 - a - b
			if c < 0:
				continue
			for x in range(len(s)+1):
				for y in range(len(s)+1):
					if a == 0 and x == 0:
						continue
					if b == 0 and x == len(s) and y == 0:
						continue
					if c == 0 and y == len(s):
						continue
					if validDouble(s, rep, a, b, c, x, y):
						#print "validDouble", a, b, c, x, y
						return True
	return False

inputfile = InputFile(sys.stdin)
T = inputfile.readInt()
for test in range(1,T+1):
	(L, X)= inputfile.readIntegers()
	s = inputfile.readString()
	assert(len(s) == L, "{0}--{1}".format(s, L))

	result = solve(s, X)
	
	if result:
		print "Case #{test}: YES".format(test=test)
	else:
		print "Case #{test}: NO".format(test=test)
