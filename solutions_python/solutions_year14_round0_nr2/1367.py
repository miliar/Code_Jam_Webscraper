#!/bin/python

iterations = raw_input() 

for iteration in range(int(iterations)) :
	parameters = (raw_input()).split(" ")
	C = float(parameters[0])
	F = float(parameters[1])
	X = float(parameters[2])
	cookie_rate = 2.0

	total_time = 0.0
	while 1 :
		next_farm = C/cookie_rate + (X)/(cookie_rate+F)
		goal_time = X/cookie_rate
		if next_farm < goal_time :
			farm_time = C/cookie_rate
			total_time = total_time + farm_time
			cookie_rate = cookie_rate + F
		else :
			total_time = total_time + goal_time
			break
		
		
	
	print "Case #%s:" % str(int(iteration+1)),
	print total_time
