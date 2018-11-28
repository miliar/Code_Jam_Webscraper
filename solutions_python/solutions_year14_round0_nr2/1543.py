def time(farm_cost, f, goal):
	spent_time = 0
	current_rate = 2.0
	time_to_recover = farm_cost/f
	while True:
		if time_to_recover > (goal - farm_cost)/ current_rate:
			return spent_time + goal/current_rate
		spent_time += farm_cost/current_rate
		current_rate += f


ncases = int(raw_input());
for i in xrange(ncases):
	farm_cost, f, goal = [float(a) for a in raw_input().split()]
	print "Case #{}: {}".format(i+1, time(farm_cost, f, goal))