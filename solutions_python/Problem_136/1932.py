#!/usr/bin/env python3

import math
from sys import stdin

C = 0
F = 0
X = 0

def time_to_spend(speed, target):
	return target / speed

#def min_time(current, speed):
#
#	if current > X:
#		return 0
#
#	direct_time = time_to_spend(speed, X-current)
#
#	buy_time = time_to_spend(speed, C-current)
#	print(current, speed, buy_time, direct_time)
#
#	if(buy_time < direct_time):
#		after_buy = min_time(0, speed+F)
#	else:
#		after_buy = 0
#
#	return min(buy_time+after_buy, direct_time)

def min_time(init_current, init_speed):
	current = [init_current]
	direct = [time_to_spend(init_speed, X)]
	speed = init_speed 

	c = 0
	d = 0

	while True:
		c = current[-1] + time_to_spend(speed, C)
		speed += F
		d = time_to_spend(speed, X)
		if c + d > current[-1] + direct[-1]:
			break;
		else:
			current.append(c)
			direct.append(d)

	return current[-1] + direct[-1]


cases = int(stdin.readline())

for case in range(1, cases+1):
	line = stdin.readline()
	C, F, X = [float(x) for x in line.split()]
	t = min_time(0.0, 2.0)
	print('Case #%d: %.7f' % (case, t))

