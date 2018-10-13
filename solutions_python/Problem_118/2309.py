#! /usr/bin/python

import math

def is_palindrome(snum):
	if len(snum) <= 1:
		return True
	elif snum[0] == snum[-1]:
		return is_palindrome(snum[1:-1])
	else:
		return False

def countFairAndSquare(a, b):
	count = 0
	for i in range(a, b+1):
		sqr = math.sqrt(i)
		if sqr % 1 == 0 and is_palindrome(str(int(i))) and is_palindrome(str(int(sqr))):
			count += 1
	
	return str(count)

ifile = open("C-small-attempt0.in", "r")

#ignore data not necessary for python fileio
cases = int(ifile.readline())

for i in range(0, cases):
	a, b = ifile.readline().rstrip(" \r\n").split()
	a, b = int(a), int(b)
	
	print "Case #" + str(i+1) + ": " + countFairAndSquare(a, b)
	

