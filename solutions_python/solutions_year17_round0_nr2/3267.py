#!/usr/bin/python

def isValid(n):
	val = 0
	for i in n:
		if int(i) < val:
			return False
		val = int(i)
	return True

def correctDigit(n):
	length = len(n)
	for i in xrange(1, length):
		if int(n[i]) < int(n[i-1]):
			prefix = n[:i-1]
			prefix += str(int(n[i-1])-1)
			correctValue = prefix + '9'*(length-i)
			#correct the digit at i-1
			return correctValue
	return n

def solve(n):
	while not isValid(n):
		n = correctDigit(n)
	while n[0]=='0':
		n = n[1:]
	return n

for i in xrange(input()):
	print "Case #"+str(i+1)+": "+solve(raw_input().strip())
