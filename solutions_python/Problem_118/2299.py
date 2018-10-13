#!/usr/bin/python

import math

def ispalindrome(word):
    return word == word[::-1]

def counFairNSquare(A,B):
	count=0
	s=0
	for x in range(A,B+1):
		s = math.sqrt(x)
		if ispalindrome(str(x)) and s.is_integer() and ispalindrome(str(math.trunc(s))):
			count+=1
	return count

f = file("C-small-attempt3.in")

cc=1
cases = int(f.readline())

while cc<=cases :
	s = f.readline().split(" ")
	A = int(s[0])
	B = int(s[1])
	print "Case #{0}: {1}".format(cc,counFairNSquare(A,B))
	cc+=1

