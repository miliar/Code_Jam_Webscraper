#!/usr/bin/python
# Zoltan Puskas <mr.zoltan.puskas@gmail.com>
# Candy

import sys

fin = open('C-large.in', 'r')
fout = open('C-large.out', 'w')

numberOfCases = int(fin.readline())
caseNum = 0;
for i in range(numberOfCases):
	caseNum += 1
	fin.readline()
	numbers = map(int, fin.readline().rstrip().rsplit(' '))
	numbers.sort()

	xorAll = 0
	sumAll = 0
	for i in numbers:
		xorAll = xorAll ^ i
		sumAll += i
	if xorAll != 0:
		print "Case #{}: NO".format(caseNum)
		result = "Case #{}: NO\n".format(caseNum)
		fout.write(result)
		continue
	else:
		print "Case #{}: {}".format(caseNum, sumAll-numbers[0])
		result = "Case #{}: {}\n".format(caseNum, sumAll-numbers[0])
		fout.write(result)

