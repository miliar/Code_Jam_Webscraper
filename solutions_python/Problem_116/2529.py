#!/usr/bin/python

import sys

T = int(sys.stdin.readline())

for i in xrange(T):
	A = ['','','','']
	for x in xrange(4):
		A[x] = sys.stdin.readline().strip('\n')
	space = sys.stdin.readline()
	
	wonX = ['XXXX','TXXX','XTXX','XXTX','XXXT']
	wonO = ['OOOO','TOOO','OTOO','OOTO','OOOT']
	testx,testo = "",""
	# ROWS
	for j in xrange(4):
		if A[j] in wonX:
			testx = "X won"
		if A[j] in wonO:
			testo = "O won"
	#COLUMNS
	for x in xrange(4):
		box = ""
		for y in xrange(4):
			box = box + A[y][x]
			if box in wonX:
				testx = "X won"
			if box in wonO:
				testo = "O won"
	#diagonal
	box1 = A[0][0] + A[1][1] + A[2][2] + A[3][3]
	if box1 in wonX:
		testx = "X won"
	if box1 in wonO:
		testo = "O won"
	box1 = A[0][3] + A[1][2] + A[2][1] + A[3][0]
	if box1 in wonX:
		testx = "X won"
	if box1 in wonO:
		testo = "O won"

	#ALL full for Draw
	for x in A:
		if '.' in x:
			testdot = 1
		else:
			testdot = 0
	if testx == "X won" and testo == "O won":
		result = "Draw"
	elif testx == "X won":
		result = "X won"
	elif testo == "O won":
		result = "O won"
	elif testdot == 1:
		result = "Game has not completed"
	elif testdot == 0:
		result = "Draw"		
	print "Case #%d: %s" %(i+1,result)