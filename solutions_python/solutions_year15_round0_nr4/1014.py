#!/usr/bin/python2.7

for case in range(input()):
	X, R, C = map(int, raw_input().split())

	sol = 'GABRIEL'
	if (((R * C) % X) != 0):
		sol = 'RICHARD'
	elif (X == 1):
		sol = 'GABRIEL'
	elif ((R == 1) or (C == 1)) and (X > 2):
		sol = 'RICHARD'
	elif (X < 4):
		sol = 'GABRIEL'
	elif (C == 2) or (R == 2):
		sol = 'RICHARD'

	print 'Case #%s: %s' % ((case + 1), sol)

