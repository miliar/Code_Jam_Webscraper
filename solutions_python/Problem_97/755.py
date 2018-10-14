#!/usr/bin/env python

import sys

def rotate(s):
    return s[1:] + s[:1]

f = open(sys.argv[1], "r")
numberOfCases = f.readline()
data = f.readlines()
case_num = 0
for line in data:
	result = 0
	case_num+=1
	bounds=line.split()
	A = int(bounds[0])
	B = int(bounds[1])
	if (B > 10):
		for n in range(A, B):
			m = str(n)
			while True:
				m = rotate(m)
				if(m == str(n)):
					break	
				if(int(m) >= A and int(n) < int(m) and int(m) <= B):
					result +=1
	
	print "Case #" + str(case_num) + ": " + str(result) 
