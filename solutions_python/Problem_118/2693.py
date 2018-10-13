#!/usr/bin/python

import math
import sys

testCase = 1
with open(sys.argv[1]) as f:
	f.readline()
	for line in f:
		AB = line.split(' ')
		A=int(AB[0])
		B=math.sqrt(int(AB[1]))
		i=1
		no=0
		while i <= B:
			i_reversed = int(str(i)[::-1])
			if i == i_reversed:
				s = i**2
				if s >= A:
					s_reversed = int(str(s)[::-1])
					if s == s_reversed:
						no += 1
			i+=1
		print "Case #"+str(testCase)+": "+str(no)
		testCase+=1
