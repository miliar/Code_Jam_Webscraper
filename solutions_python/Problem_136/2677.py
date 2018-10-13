#!/usr/bin/python

for case in range(1,int(raw_input())+1):          #For all test cases
	C, F, X = map(float, raw_input().split(" "))

	seconds = 0
	ratio = 2
	farm_ratio = F

	while (True):
		next_farm = C/ratio
		next_farm_ratio = (ratio+farm_ratio)
		cur_end_time = X/ratio
		next_farm_end_time = next_farm + X/next_farm_ratio

		if (next_farm_end_time >= cur_end_time):
			seconds += cur_end_time
			break
		else:
			seconds += next_farm
			ratio = next_farm_ratio

	print "Case #%d: %.7f" % (case, seconds)

