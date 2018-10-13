#!/usr/bin/python

import sys

def getDigits(num):
	d = []
	npos = 0
	while num>0:
		d.append(num % 10)
		npos += 1
		num = num / 10
	return d, npos

def listToNum(l):
	i = 1
	num = 0
	for d in l:
		num += d*i
		i *= 10
	return num

def moveDigits(digits,pos):
	tmp = []
	tmp.extend(digits[pos:])
	tmp.extend(digits[:pos])
	return tmp

def countPairs(num,end):
	digits,npos = getDigits(num)
	pos = 1
	ncount = 0
	while pos<npos:
		newdigits = moveDigits(digits,pos)
		newnum = listToNum(newdigits)
		if (newnum > num) and (newnum <= end):
			ncount += 1
		pos += 1
	return ncount

def doProcess(begin, end):
	ncount = 0
	while (begin < end):
		ncount += countPairs(begin,end)
		begin = begin + 1
	return ncount

inp = sys.stdin

T = int(inp.readline())

n = T

while n>0:
	l = inp.readline().split()
	begin,end = int(l[0]), int(l[1])
	print "Case #"+str(T-n+1)+": "+str(doProcess(begin,end))
	n = n - 1

