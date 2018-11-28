#!/usr/bin/env python
#print "Intranet program v1.0"
from math import *

cases = int(raw_input())
for c in xrange(cases):
	# read in misc problem constants

	# read in data
	outstr = ""
	tmp = []
	data = []
	strBoard = []
	for i in range(5):
		try:
			tmp = map(str,raw_input().split())
		except(EOFError):
			break
		if len(tmp) == 1:
			data.append(list(tmp[0]))
	#print data
	#for i in range(4):
	#	for j in range(4):
	#		#print data[i][j], i , j
	chars = ['X', 'O']
	for matchChar in chars:
		for i in range(4):
			if (data[i][0] == matchChar or data[i][0] == 'T') and \
			(data[i][1] == matchChar or data[i][1] == 'T') and \
			(data[i][2] == matchChar or data[i][2] == 'T') and \
			(data[i][3] == matchChar or data[i][3] == 'T'):
				outstr = "%s won" % matchChar
				break
		for j in range(4):
			if (data[0][j] == matchChar or data[0][j] == 'T') and \
			(data[1][j] == matchChar or data[1][j] == 'T') and \
			(data[2][j] == matchChar or data[2][j] == 'T') and \
			(data[3][j] == matchChar or data[3][j] == 'T'):
				outstr = "%s won" % matchChar
				break
		if (data[0][0] == matchChar or data[0][0] == 'T') and \
		(data[1][1] == matchChar or data[1][1] == 'T') and \
		(data[2][2] == matchChar or data[2][2] == 'T') and \
		(data[3][3] == matchChar or data[3][3] == 'T'):
			outstr = "%s won" % matchChar
			break

		if (data[0][3] == matchChar or data[0][3] == 'T') and \
		(data[1][2] == matchChar or data[1][2] == 'T') and \
		(data[2][1] == matchChar or data[2][1] == 'T') and \
		(data[3][0] == matchChar or data[3][0] == 'T'):
			outstr = "%s won" % matchChar
			break

	if outstr == "":
		dots = False
		for i in range(4):
			for j in range(4):
				if data[i][j] == '.':
					dots = True
					break
		if dots == True:
			outstr = "Game has not completed"
		else:
			outstr = "Draw"

	# problem solving logic here	
	
	# output answer
	print "Case #%d:" % (c+1), outstr
	