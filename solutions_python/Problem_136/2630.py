#!/usr/bin/python

import sys

n = int(sys.stdin.readline())
for i in range(1, n + 1):
	sys.stdout.write("Case #" + str(i) + ": ")

	args = sys.stdin.readline().split()
	c = float(args[0])
	f = float(args[1])
	x = float(args[2])
	
	t = 0.0
	rate = 2.0

	while True:
		ttx = x / rate
		ttf = c / rate

		if ttx < ttf:
			print str(t + ttx)
			break

		rate += f
		ttxwf = ttf + (x / rate)

		if ttx < ttxwf:
			print str(t + ttx)
			break

		t += ttf
