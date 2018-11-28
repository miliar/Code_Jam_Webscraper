#! /usr/bin/env python
from math import sqrt
import fileinput

number = 121

def isFairAndSquare(n):
	if not isPalindrome(int(n)):
		return False;
	if isSquareOfPalindrome(n):
		return True;
	return False;

def isPalindrome(n):
	if str(n) == str(n)[::-1]:
		return True
	return False

def isSquareOfPalindrome(n):
	sn = sqrt(float(n))
	if sn == int(sn):
		if isPalindrome(int(sn)):
			return True
	return False

c = 0
for line in fileinput.input(files=('C-small-attempt5.in')):
	c+=1
	fl= line.split()
	i = 0
	for number in xrange( int(fl[0]), int(fl[1])+1 ):
		if isFairAndSquare(number):
			i+=1
	print "Case #"+str(c)+": "+str(i)