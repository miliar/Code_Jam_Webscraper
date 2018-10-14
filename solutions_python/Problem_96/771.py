#!/usr/bin/env python

import sys
from array import *


f = open(sys.argv[1], "r")
numberOfCases = f.readline()
data = f.readlines()
case_num = 0
for line in data:
	result = 0
	case_num+=1
	data=line.split()
	NumGooglers = int(data[0])
	Scores = array('f')
	NumSuprising = int(data[1])
	MinScore = int(data[2])
	for Googler in range(0, NumGooglers):
		Scores.insert(Googler,int(data[3+Googler]))
	for MyScore in Scores:
		s=round(MyScore/3)
		if(MyScore%3 == 0):
			if(s >= MinScore):
				result+=1
			else:
				if(NumSuprising > 0 and s+1-MinScore == 0 and MinScore > 1):
					result+=1
					NumSuprising-=1
		if(MyScore%3 == 1):
			if(s+1 >= MinScore):
				result+=1
		if(MyScore%3 == 2):
			if(s >= MinScore):
				result+=1
			else:
				if(NumSuprising > 0 and s+1-MinScore == 0 and MinScore > 2):
					result+=1
					NumSuprising-=1
	print "Case #" + str(case_num) + ": " + str(result) 
			
