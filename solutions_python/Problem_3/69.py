#!/usr/bin/env python

from string import split, join, strip
from sys import argv, stdin, exit
from copy import copy
import math

LINES_PER_CASE = None

global STEP


def solve(case):
	global STEP

	(Fr, Or, T, Sr, G) = map(float, split(case))
	
	Sd = 2.0 * Sr
	Fd = 2.0 * Fr
	
	Ir = Or - T
	IrSq = Ir * Ir

	if (G <= Fd):
		return '1.000000'
	
	FHA = (G - Fd) * (G - Fd)
	TotArea = Or * Or * math.pi
	RaqS = int(math.ceil( (Or-T-Sr) / (G+Sd) ))
	
	STEP = (RaqS * G) / 500000.0

	Raq = []
	# matrix overlapping 1/4 of raquet	
	for i in range(RaqS):
		Raq.append( [0.0] * RaqS )

	unit = G + Sd
	
	for y in range(RaqS):
		b = Sr + y * (unit)
		t = b + G
		for x in range(RaqS):
			l = Sr + x * (unit)
			r = l + G
			
			# fully in
			if (math.hypot(r, t) <= Ir):
				Raq[RaqS-1-y][x] = FHA
			# fully out
			elif (math.hypot(l, b) >= Ir):
				pass
			else:
				tmp = pseudo_integral(Ir-Fr, l+Fr, r-Fr, b+Fr, t-Fr)
				if (tmp < 0.0):
					tmp = 0.0
				elif (tmp > FHA):
					tmp = FHA
				Raq[RaqS-1-y][x] = tmp
			
#	for r in Raq:
#		print r

	HoleArea = 0.0
	for x in range(RaqS):
		HoleArea = HoleArea + sum(Raq[x])
	
	HoleArea = HoleArea * 4.0
	
#	print 'HoleArea', HoleArea
#	print 'TotArea', TotArea

	ret = (1.0 - HoleArea / TotArea)
	
	if (ret < 0.00000001):
		ret = 0.0

	return '%.6f' % (ret)


def pseudo_integral(Ir, l, r, b, t):
	global STEP
	area = 0
	#step = (r - l) / 100.0
	STEP = (r - l) / 50000.0
	l = l + STEP/2.0
	IrSq = Ir * Ir
	while (True):
		a = h(IrSq, l, r, b, t)
		assert(not a < 0)
		if (a == 0):
			break
		area = area + a * STEP
		l = l + STEP
	return area


def h(IrSq, l, r, b, t):
	if (l > r):
		return 0.0
	tmp = IrSq - (l*l)
	if (tmp < 0):
		return 0
	y = math.sqrt( tmp )
	if (y < b):
		return 0.0
	if (y > t):
		return (t-b)
	return (y-b)




def main():
	global LINES_PER_CASE
	
	f = open(argv[1])

	cases = int(f.readline())

	specific_case = None
	if (len(argv) > 2):
		if (argv[2][0] == '.'):
			specific_case = int(argv[2][1:])
		else:
			max_cases = int(argv[2])
			if (max_cases < cases):
				cases = max_cases

	for c in range(1, cases+1):
		cd = strip(f.readline())
		if (specific_case):
			if (c != specific_case):
				continue
			else:
				print cd

		print 'Case #' + str(c) + ": " + solve(cd)

main()
