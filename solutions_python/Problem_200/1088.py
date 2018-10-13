#!/usr/bin/env python

def TidyNumber(num):
	smallest = 10
	digs = [int(dig) for dig in num[::-1]]

	for idx, dig in enumerate(digs):
		if dig > smallest:
			smallest = digs[idx] = dig - 1
			digs[ :idx] = [9] * idx
		else:
			smallest = dig

	return ''.join(map(str, digs[::-1])).lstrip('0')

fileOut = open('file.out', 'w')

with open('file.in', 'r') as fileIn:
	for i in xrange(int(fileIn.readline())):
		fileOut.write('Case #{}: {}\n'.format(i + 1, TidyNumber(fileIn.readline().strip())))

fileIn.close()
fileOut.close()
