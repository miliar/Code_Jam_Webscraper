#!/usr/bin/env python
# encoding: utf-8

import sys, os, re

f = open('./input.txt')
o = open('./output.txt', 'w')
T = int(f.readline())

def time_farm_or_cookie(C, F, s):
	return C * (1 / F + 1 / s)

for case in range(1, T+1):
	n = map(float, f.readline().split(' '))
	C = n[0] # farm price
	F = n[1] # farm cookie/sec
	X = n[2] # goal
	s = 2.0 # 2 cookies/sec
	t = 0.0
	finish = False

	while not finish:
		tt = time_farm_or_cookie(C, F, s)

		if X <= tt * s:
			t += X / s #round(t + X / s, 7)
			finish = True
		else:
			t += C / s #round(t + C / s, 7)
			s += F

	t = round(t, 7)
	o.write("Case #%s: %s\n" % (case, t))

f.close()
o.close()
