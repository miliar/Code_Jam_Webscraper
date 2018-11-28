#!/usr/bin/python

import sys
import math

MAX_AB = math.pow(10, 100)

"""
class sqtable():
	sqt = []
	def __init__(self, maxvalue):
		self.makesqtable(maxvalue)
	def makesqtable(self, maxvalue):
		for i in range(0, int(math.sqrt(maxvalue))):
			self.sqt.append(i * i)
	def getsqt(self):
		return self.sqt
	def have(self, num):
		return self.sqt.find(num)
"""

def isfair(num):
	return str(num) == str(num)[::-1]

def issquare(num):
	r = int(math.sqrt(num))
	return ((r * r) == num) and isfair(r)

def main(f):
	fp = open(f, 'rt')
	cases = int(fp.readline())

	for i in range(cases):
		(a, b) = fp.readline().split()
		a = int(a)
		b = int(b)
		count = 0

		for j in range(a, b + 1):
			if isfair(j) and issquare(j):
				#print 'true in : ' + str(j)
				count += 1
		print 'Case #%d: %d' % (i + 1, count)
	return


if __name__ == '__main__':
	if len(sys.argv) == 1:
		print 'no input file'
		exit(-1)
	main( sys.argv[1] )
