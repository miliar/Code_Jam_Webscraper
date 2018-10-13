#!/usr/bin/python3

import sys

def parseLine(inputfile):
	return tuple([float(x) for x in inputfile.readline().split()])

def compute(c,f,x):
	farms = 0.0
	cookies = 0.0
	time = 0.0
	while (cookies < x):
		if (cookies >= c):
			if (((x - cookies) / (2.0 + (farms * f))) < (((x - cookies) + c) / (2.0 + (f * (farms + 1.0))))):
				time += (x - cookies) / (2.0 + (farms * f))
				cookies = x
			else:
				cookies -= c
				farms += 1
		else:
			if ((x - cookies) < (c - cookies)):
				time += ((x - cookies) / (2.0 + (farms * f)))
				cookies = x
			else:
				time += ((c - cookies) / (2.0 + (farms * f)))
				cookies = c
	return time

if (len(sys.argv) == 2):
	text = open(sys.argv[1],'r')

	testCount = int(text.readline())
	
	for i in range(testCount):
		c,f,x = parseLine(text)
		#print("C: {}\nF: {}\nX: {}\n".format(c,f,x))
		print("Case #{}: {}".format(i+1, compute(c,f,x)))
