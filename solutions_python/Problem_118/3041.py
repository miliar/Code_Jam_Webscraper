#!/usr/bin/python
# -*- coding: utf-8 -*-

from string import *
from math import *

def isPalin(number):
	if str(number) == str(number)[::-1]:
		return 1
	else:
		return 0

def check(line):
	rslt = 0
	newLine = line.split(' ')
	A = int(newLine[0])
	B = int(newLine[1][0:-1])
	print A,B
	for numb in range(A,B+1):
		if isPalin(numb):
			sqrtNumb = sqrt(numb)
			if isPalin(int(sqrtNumb)) & (str(sqrtNumb).split('.')[1] == "0"):
				rslt += 1
	return rslt

def writeFile(nbLine, nb):
	outp = open('./output.in',"a")
	toWrite = "Case #%d: %d\n" % (nbLine, nb)
	outp.write(toWrite)
	outp.close()

def readFile():
	f = open('./thefile.in', "r")
	lines = f.readlines()

	i = 0
	for line in lines:
		if i == 0:
			i+=1
			pass
		else:
			i+=1
			rslt = check(line)
			writeFile(i-1,rslt)

print "GO !"
readFile()
print "Finish !"