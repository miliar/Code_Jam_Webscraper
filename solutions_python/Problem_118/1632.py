#!/usr/bin/env python
#print "Intranet program v1.0"
from math import *

# for small cases
minA = 1
maxB = 1e14
maxSquare = int(sqrt(maxB))

#preCoumputed to 1e14
fairsquare14 = [1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004]


def isPalindrome(x):
	y = x[::-1]
	if x==y:
		return True 
	return False 

#	fairsquare = []
#	for i in range(1,maxSquare+1,1):
#		if isPalindrome(str(i)):
#			if isPalindrome(str(i**2)):
#				fairsquare.append(i**2)
#	print fairsquare

cases = int(raw_input())
for c in xrange(cases):
	# read in misc problem constants

	# read in data
	tmp = []
	data = []
	try:
		tmp = map(str,raw_input().split())
	except(EOFError):
		break
	for i in tmp:
		data.append(int(i))
	#print data
	
	
	lowSlice = 0
	highSlice = 0
	for i in fairsquare14:
		if i >= data[0]:
			lowSlice = fairsquare14.index(i)
			#print lowSlice
			break
	for i in reversed(fairsquare14):
		if i <= data[1]:
			highSlice = fairsquare14.index(i)
			#print highSlice
			break
	
			
	# output answer
	print "Case #%d:" % (c+1), highSlice - lowSlice + 1
	