#!/usr/local/bin/python

import sys
from fractions import gcd

def getDiff(list):
	diff = []
	for i in range(1, len(list)):
		diff.append(list[i] - list[i-1])
	return diff


def getDivisor(list):
	divisor = list[0]
	for item in list:
		divisor = gcd(divisor, item)
	return divisor


if __name__ == "__main__":
	f = open(sys.argv[1])
	for i in range(int(f.readline())):
		list = f.readline().split()
		list = list[1:]
		list = map(int, list)
		list.sort()
		diff = getDiff(list)
		commonDivisor = getDivisor(diff)
		if list[0] % commonDivisor == 0:
			result = 0
		else:
			result = commonDivisor - list[0] % commonDivisor
		print "Case #%d: %d" % (i+1, result)
