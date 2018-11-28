#!/usr/bin/env python

import sys, math

#### BEGIN STUFF TO CACHE FAIR AND SQUARES ####

def nextpalindrome(num):
	s = str(num)
	n = len(s)

	if n == 1:
		return num + 1

	if n % 2 > 0: # odd
		lhs = s[:math.floor(n/2)]
		rhs = s[math.ceil(n/2):][::-1]
		c = s[math.floor(n/2):math.ceil(n/2)]

		if int(lhs) <= int(rhs):
			if c == 9:
				lhs = str(int(lhs) + 1)
				c = "0"
			else:
				c += str(int(c) + 1)

		return int(lhs + c + lhs[::-1])

	else: # even
		lhs = s[:int(n/2)]
		rhs = s[int(n/2):][::-1]

		if int(lhs) <= int(rhs):
			lhs = str(int(lhs) + 1)

		return int(lhs + lhs[::-1])

def ispalindrome(num):
	s = str(num)
	n = len(s)

	if n % 2 > 0:
		return s[:math.floor(n/2)] == s[math.ceil(n/2):][::-1]
	else:
		return s[:int(n/2)] == s[int(n/2):][::-1]

def create_fairandsquare(fairfile):
	f = open(fairfile, 'w+')

	cur = 1
	num = 1
	# WARNING: This takes a while to run
	while cur <= 10**100:
		cur = num**2
		if ispalindrome(cur):
			f.write(str(cur) + '\n')

		num = nextpalindrome(num)

 # NOTE: Previous stuff is performed prior to attempting any data sets
 # I don't believe there is anything in the rules against this...


#### BEGIN PROGRAM #####

if len(sys.argv) > 1:
	input = sys.argv[1]
else:
	input = "input.txt"

if len(sys.argv) > 2:
	fairfile = sys.argv[2]
else:
	fairfile = "fairsquare.txt"

try:
	with open(input) as f:
		content = [[int(c) for c in line.split()] for line in f.readlines()]
except:
	print("Can not find input file: %s" % input)
	sys.exit()

# Make sure we have our fair and square values!
try:
	with open(fairfile) as fs:
		fairsquares = [int(f) for f in fs.readlines()]
except FileNotFoundError:
	print("ERROR: Fair and square file (%s) does not exist... creating" % fairfile)
	create_fairandsquare(fairfile)
	print("Done! Please re-run the program")
	sys.exit()

T = int(content[0][0])

case = 1
while case <= T:
	result = 0
	A, B = content[case]

	count = 0
	for i in fairsquares:
		if i >= A and i <= B:
			count += 1

	print("Case #%d: %d" % (case, count))

	case += 1


