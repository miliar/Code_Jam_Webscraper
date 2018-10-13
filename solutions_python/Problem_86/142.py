#!/usr/local/bin/python

# C. Perfect Harmony

import math
import sys
from fractions import gcd


def lgcd(list):
	GCD = list[0]
	for e in list:
		GCD = gcd(GCD, e)
	return GCD

def lcm(num1, num2):
	result = num1*num2/gcd(num1,num2)
	return result

f = sys.stdin
T = int(f.readline())

for x in range(1, T+1):
	list = [int(e) for e in f.readline().split()]
	N = int(list[0])
	L = int(list[1])
	H = int(list[2])
	list = [int(e) for e in f.readline().split()]
	#list.sort()

	y = "NO"
	for i in range(L, H+1):
		ok = True
		for e in list:
			if (e >= i and e % i == 0) or (e <= i and i % e == 0):
				pass
			else:
			 	ok = False
			 	break
		if ok:
			y = i
			break

	s = """
	LCM = lgcd(list)
	if L <= LCM and LCM <= H:
		print "Case #%d: %s" % (x, y)
		continue

	for i in range(N):
		LCM = lcm(LCM, list[i])
		ok = True
		for j in range(i+1, N):
			if list[j] % LCM != 0:
				ok = False
				break
		if ok and L <= LCM and LCM <= H:
			y = LCM
			break
			"""

	print "Case #%d: %s" % (x, y)
