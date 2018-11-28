#!/usr/bin/env python2.7
import math

def is_palindrome(n):
	number = str(n)
	for i in xrange(len(number)/2):
		if number[i] != number[len(number)-1-i]:
			return False
	return True

T = int(raw_input())

for t in xrange(T):
	numbers = raw_input().split()
	A, B = int(numbers[0]), int(numbers[1])

	a = int(math.ceil(math.sqrt(A)))
	b = int(math.floor(math.sqrt(B)))
	
	count = 0
	for i in xrange(a,b+1):
		if is_palindrome(i**2) and is_palindrome(i):
			count += 1
	
	print "Case #%d:" % (t+1), count
