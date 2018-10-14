#!/bin/bash

T = int(raw_input())

for i in xrange(T):
	(C,F,X) = [float(x) for x in raw_input().split(" ")]
	cookies = 0.0
	rate = 2.0
	t = 0.0
	while cookies < X - 1e-6: # based on iterations to farms
		dt1 = (C - cookies) / rate # time to achieve the next farm based on current rate
		dt2 = C / F # time for buying a farm to break even
		x2 = dt2 * (rate + F) # rate at which we break even
		if x2 >= X - 1e-6: # if the breakeven point is > X, we should not buy new farm
			dt = dt1 + (X - C) / rate # (X - C) / rate is the time it wil take to achieve our goal
			t += dt
			cookies += dt * rate
		else: # otherwise, we should greedily buy farm
			cookies += dt1 * rate - C # update cookies, is probably 0
			t += dt1
			rate += F
	print("Case #%d: %.7f" % (i+1, t))
