#!/usr/bin/env python2.7

from decimal import *

def solve(filename):
	i = open(filename, "Ur")
	out = open("out1", "w")
	l = i.readlines()
	num = int(l[0])
	getcontext().prec = 40
	for y in range(num):
		v = l[y+1].split()
		r = Decimal(v[0])
		p = Decimal(v[1])
		ans = int((1 - 2 * r + ((2 * r - 1) ** 2 + p * 8).sqrt()) / 4)
		out.write("Case #" + str(y + 1) + ": " + str(ans) + "\n")
	out.close()
	i.close()

solve("in1")
