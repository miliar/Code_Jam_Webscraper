import sys

with open(sys.argv[1]) as f:
	f.next()
	for case_number, case in enumerate(f, 1):
		farm_cost, farm_boost, goal = map(float, case.strip().split())
		time = 0
		farms = 0
		while(True):
			next_farm = farm_cost / (2 + farm_boost * farms)
			goal_time = goal / (2 + farm_boost * farms)
			goal_time_with_farm = next_farm + goal / (2 + farm_boost * (farms + 1))
			if goal_time_with_farm < goal_time:
				time += next_farm
				farms += 1
			else:
				print 'Case #%s: %.7f' % (case_number, time + goal_time)
				break