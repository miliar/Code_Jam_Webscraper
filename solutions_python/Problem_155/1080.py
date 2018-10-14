#!/usr/bin/python
# -*-coding:Latin-1 -*
import os
T = input()
for i in range(0,T):
	line = raw_input()
	var = line.split()
	x = int(var[0])
	case = var[1]
	numb = 0
	need = 0
	for j in range(0,x+1): 
		if  numb < j:
			need +=1 
			numb +=1
		numb += int(case[j]) 
	print "case #" + str(i+1) +": "+ str(need)
