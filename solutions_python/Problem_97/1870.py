#!/usr/bin/python2

from collections import deque

def getNumPairs(l, h, num):
	counter = 0
	ms = []
	if num < 9:
		return 0
	elif num < 99:
		if palindrome(num) >= l and palindrome(num) <=h and palindrome(num) > num:
			return 1
		else:
			return 0
	else:
		for i in xrange(1, numDigits(num)):
			m = rot(num, i)
			if m >= l and m <= h and m > num:
				if m not in ms:
					counter+=1
				ms.append(m)
		return counter

def palindrome(num):
	return (num % 10) * 10 + num / 10

def numDigits(num):
	return len(str(num))

def rot(num, n):
	d = deque(str(num))
	d.rotate(n)
	return int("".join(d))

if __name__ == "__main__":
	output = ""
	numTestCases = raw_input()
	numTestCases = int(numTestCases)
	for i in xrange(0, numTestCases):
		limits = raw_input()
		l = int(limits.split(" ")[0])
		h = int(limits.split(" ")[1])
		counter = 0
		for j in xrange(l, h+1):
			counter += getNumPairs(l, h, j)
		output += "Case #"+str(i + 1)+": "+str(counter)
		output += "\n"

	print output