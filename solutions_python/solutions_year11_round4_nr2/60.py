#!/usr/bin/env python

import sys

def check_balance(sheet, x0, x1, y0, y1):
# 	print
	x_mid = x0 + (x1 - x0) / 2.0
	y_mid = y0 + (y1 - y0) / 2.0
	x_tot = 0
	y_tot = 0
# 	print x_mid, y_mid
	for i in xrange(x0, x1 + 1):
		for j in xrange(y0, y1 + 1):
			if (i == x0 or i == x1) and (j == y0 or j == y1):
				continue
			x = i
			y = j
# 			print x_tot, y_tot, '\t', 'pos', x, y, sheet[i][j], '\t',
			x_tot += sheet[i][j] * (x - x_mid)
			y_tot += sheet[i][j] * (y - y_mid)
# 			print x_tot, y_tot
# 	print x0, x1, x_tot, y_tot
	return x_tot == 0.0 and y_tot == 0.0

cases = int(sys.stdin.readline())

for case in xrange(1, cases + 1):
	print "Case #%d:" % case,
	R, C, D = [int(v) for v in sys.stdin.readline().strip().split()]
	sheet = []
	for i in xrange(R):
		line = [int(v) for v in sys.stdin.readline().strip()]
		sheet.append(line)
	
	best = -1
	for x0 in xrange(R):
		for y0 in xrange(C):
			for x1 in xrange(x0 + 2, R):
				d = x1 - x0
				y1 = y0 + d
				if y1 >= C:
					continue
# 				print d + 1, x0, y0,
				if d >= best and check_balance(sheet, x0, x1, y0, y1):
# 					print 'yes!',
					best = d + 1
# 				print
	
	if best < 0:
		print "IMPOSSIBLE"
	else:
		print best
