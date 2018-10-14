count = int(raw_input())
for i in range(count):
	ans = -1
	numbers = map(float, raw_input().split())
	farm_cost = numbers[0]
	farm_rate = numbers[1]
	production_rate = 2
	last_seconds = 0
	goal = numbers[2]
	while ans < 0:
		timeA = goal/production_rate
		newFarmT = (farm_cost/production_rate)
		timeB = newFarmT + (goal/(production_rate+farm_rate))
		if timeA < timeB:
			ans = timeA+last_seconds
			break
		else:
			last_seconds += newFarmT
			production_rate += farm_rate
	print "Case #" + str(i+1) + ":", "%.7f" % ans
