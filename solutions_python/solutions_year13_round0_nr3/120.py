#!/usr/bin/python

# C. Fair and Square

import sys
import math

splist = [1, 4, 9 ]

def isPalindrome(n):
	return n == n[::-1]

def init(B):
	for i in range(1, B):
		n = int(bin(i)[2:] + bin(i)[:1:-1])
		if isPalindrome(str(n*n)):
			splist.append(n*n)
		else: 
			continue
		n = int(bin(i)[2:] + '0' + bin(i)[:1:-1])
		if isPalindrome(str(n*n)):
			splist.append(n*n)
		else:
			continue
		n = int(bin(i)[2:] + '1' + bin(i)[:1:-1])
		if isPalindrome(str(n*n)):
			splist.append(n*n)
		else:
			continue
		n = int(bin(i)[2:] + '2' + bin(i)[:1:-1])
		if isPalindrome(str(n*n)):
			splist.append(n*n)
		else:
			continue

	base = 2
	for i in range(25):
		n = int(str(base) + str(base)[::-1])
		splist.append(n*n)
		n = int(str(base) + '0' + str(base)[::-1])
		splist.append(n*n)
		n = int(str(base) + '1' + str(base)[::-1])
		splist.append(n*n)
		base *= 10

	splist.sort()


f = sys.stdin
T = int(f.readline())

init(2**25)

for t in range(1, T+1) :
	A, B = [int(i) for i in f.readline().split()]

	count = 0
	for n in splist:
		if A <= n and n <= B:
			count += 1

	print "Case #%d: %d" % (t, count)
