#! /usr/bin/env python

import sys

T = int(sys.stdin.readline())

for case in range(1, T+1):
	V = 2.0 # Velocity
	cookies = 0.0
	t = 0.0
	C, F, X = sys.stdin.readline().split()
	C = float(C)
	F = float(F)
	X = float(X)
	
	while True:
		# Decide only when we have enough cookies. Otherwise just wait until we have enough cookie to think about. 
		if cookies >= C:
			t_wait = (X - cookies) / V
			t_buy = (X - cookies + C) / (V + F)
			if t_buy < t_wait:
				# buy
				V += F
				cookies -= C
			else:
				# wait
				cookies += t_wait*V
				t += t_wait
				if cookies >= X:
					print "Case #%d: %.7f" % (case, t)
					break
		else:
			t_wait = (C - cookies)/V
			cookies += t_wait*V
			t += t_wait
