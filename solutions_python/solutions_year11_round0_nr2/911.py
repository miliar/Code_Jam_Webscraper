#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Haley Proctor on 2010-12-18.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

import sys
import os
from math import *

def main():
	results = []
	smallinput = 'B-small-attempt0.in.txt'
	largeinput = 'B-large.in.txt'	
		
	testcases = getInput(largeinput)
	#tests = [[1], [2], [3]]
	#for i in range(1, len(tests), 2):
	#	testcases.append([tests[i], tests[i+1]])	
	#print testcases	
	
	#testcases = [1,
	#'0 0 2 EA',
	#'1 QRI 0 4 RRQR',
	#'1 QFT 1 QF 7 FAQFDFQ',
	#'1 EEZ 1 QE 7 QEEEERA',
	#'0 1 QW 2 QW'
	#]
	
	for case in testcases[1:]:
		results.append(magicka(case))
	
	for i in range(len(results)):
		print testcases[i+1], results[i]
	
			
	printOutput(results)
	printOutput(results, 'B-large-results.txt')
		



def magicka(testcase):
	combinations = {}
	opposed = {}
	
	num = int(testcase.partition(' ')[0])
	testcase = testcase.partition(' ')[2]
	for i in range(num):
		combination = testcase.partition(' ')[0]
		combinations[combination[0:-1]] = combination[-1]
		combinations[combination[::-1][1:]] = combination[-1]
		testcase = testcase.partition(' ')[2]
		
	num = int(testcase.partition(' ')[0])
	testcase = testcase.partition(' ')[2]
	for i in range(num):
		opp = testcase.partition(' ')[0]
		if opp[0] in opposed:
			opposed[opp[0]].append(opp[1])
		else:
			opposed[opp[0]] = [opp[1]]	
		if opp[1] in opposed:
			opposed[opp[1]].append(opp[0])
		else:
			opposed[opp[1]] = [opp[0]]
		testcase = testcase.partition(' ')[2]
	
	sequence = testcase.partition(' ')[2]
	
	played = []
	destroyers = {}
	for char in sequence:
		if played:
			if char + played[-1] in combinations:
				played[-1] = combinations[char+played[-1]]
			else:
				if played[-1] in opposed:
					for opp in opposed[played[-1]]:
						destroyers[opp] = 1
				if char in destroyers:
					played = []
					destroyers = {}
				else:
					played.append(char)	
		else:
			played.append(char)
	#if played[-1] in destroyers:
#		played = []			
	return played		
									
				 		
	
	

	
	

def robots(buttons):
	oPos = 1
	bPos = 1
	oTime = 0 
	bTime = 0
	time = 0
	
	print "input",buttons
	butList = []
	buttons = buttons.partition(' ')[2]
	while buttons:
		col = buttons.partition(' ')[0]
		buttons = buttons.partition(' ')[2]
		location = buttons.partition(' ')[0]
		butList.append((col, location))
		buttons = buttons.partition(' ')[2]
		
	for but in butList:
		loc = int(but[1])
		if but[0] == 'O':
			if abs(loc - oPos) <= time - oTime:
				time += 1
			else:
				time += abs(loc - oPos) - (time - oTime) + 1
			oPos = loc
			oTime = time
		if but[0] == 'B':
			if abs(loc - bPos) <= time - bTime:
				time += 1
			else:
				time += abs(loc - bPos) - (time - bTime) + 1
			bPos = loc
			bTime = time
	
	print 'time', time	
	return time		

					
def numbers(n):
	last3 = int(((3+sqrt(5))**n)%1000)/1
	return str(last3).zfill(3)

def rankispure(n, maxint, length= ''):
	total = 0
	if n == 1 or length == 1:
		return 1
	else:
		for i in range(1,n):
			if length == '':
				total+= rankispure(i, maxint)
			else:
				total+= rankispure(i, maxint, i) * (factorial(maxint-i-1)/factorial(length-n))
		return total

def themepark(line1, groups):		
	R = line1[0] #number of rides
	k = line1[1] #number of spots per ride
	
	revenue = {}
	totalrev = 0
	
	# [qstart, revenue, cumulativerevenue]
	rides = [[0,0,0]]
	qstarts = {}
	#cumulativegroups = [[groups[0],groups[0]]]
	#for group in groups[1:]:
	#	cumulativegroups.append([group, cumulativegroups[-1][-1]+ group])
	#queuesize = cumulativegroups[-1][-1]
	
	r, qstart = 0, 0
	print R, k
	rev = 0
	while qstart not in qstarts and r < R:
		
		i = qstart
		riders = 0
		rev = 0
		while riders < k and i < len(groups):
			#print qstart
			if riders + groups[i%len(groups)] < k:
				rev += groups[i%len(groups)]
			riders += groups[i%len(groups)]	
			i += 1			
		rides.append([qstart, rev, rides[-1][2] + rev])
		r += 1
		qstarts[qstart] = rev
		qstart = (i-1)%len(groups)
	del rides[0]
	
	
	if r < R: #there is a cycle
		cyclerev = rev - qstarts[qstart]
		cyclestartlocation = -1
		i=0
		while i < len(rides) and cyclestartlocation == -1:
			if rides[i] == qstart:
				cyclestartlocation = i
			i += 1	 
		cyclesize = len(rides) - cyclestartlocation
		numcycles = int(R/cyclesize)
		offset = cyclesize - R%cyclesize
		totalrev = numcycles * cyclerev + rides[cyclestartlocation - offset][2]	
		 
	else:
		totalrev = rides[-1][-1]
			
	print totalrev	
	return totalrev		
			
	
	#cumulative revenue after ride is finished
	
	#queue = groups[:]
	
	
	#r = 0
	#while r <= R and group not in :
	#	spotsleft = k
	#	while 
		
	
		
	

def slarbo(n, dates):
	
	print dates
	diffs = []
	for i in range(1,len(dates)):
		if dates[i] != dates[0]:
			diffs.append(abs(dates[i]- dates[0]))
	gcd = get_gcd(diffs)
	return (gcd-(dates[0] % gcd))%gcd	
		


def snapper(n, k):
	minsnaps =  2**n -1
	if k == minsnaps or (k-minsnaps)%(minsnaps+1) ==0:
		result = 'ON'
 	else:
		result = 'OFF'	 
	return result



def get_gcd(array):
	
	array.sort()
	gcd = array[0]
	for i in range(len(array)):
		for j in range(i, len(array)):
			b, a = array[i], array[j] 
			while b != 0:
				temp = b
				b = a % b
				a = temp
		 	if a < gcd:
				gcd = a
	return gcd			
	

def is_prime(n):
	i = 2
	while i <= sqrt(n):
		if n%i == 0:
			return False
		i += 1
	return True	


def factorial(n):
	if n == 0: 
		return 1
	f = n
	for i in range(1, n):
		f *= i
	return f


def getInput(infile='', delim=' '):
	testcases = []
	openinput = open(infile, 'r')
	for line in openinput:
		line = line.partition('\n')[0]
		testcases.append(line)
	return testcases	


def getInputFile(infile):
	return open(infile, 'r')

def printOutput(output, outputfile=''):
	if outputfile != '':
		out = open(outputfile, 'w')
	for j in range(len(output)):
		if outputfile == '':
			print 'Case #' + str(j+1) + ': ' + str(output[j]).replace("'", '')
		else:
			out.write('Case #' + str(j+1) + ': ' + str(output[j]).replace("'", '') + '\n')


if __name__ == '__main__':
	main()

