#!/usr/bin/env python
import sys


def process(C, F, X):
	speed = 2.0
	time = 0.0
	time_accelerated  = X / speed
	while True:
		time_to_next_farm = C / speed
		time_current = time_accelerated 
		time_accelerated = X / (speed + F)
		if time_to_next_farm + time_accelerated > time_current:
			time += time_current
			break
		time += time_to_next_farm
		speed += F
	return round(time, 7)

input_file = open(sys.argv[1], 'r')
T = int(input_file.readline())
for i in range(T):
	(C, F, X) = map(float, input_file.readline().split())
	print 'Case #%d:' % (i + 1), process(C, F, X)
