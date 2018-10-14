
numCases = int(raw_input())
for case in range(numCases):
	c, f, x = map(float, raw_input().split(' '))
	rate = 2.0
	time = 0.0
	prev = 0
	
	while True:
		timeToGoal = time + x / rate
		timeToFarm = time + c / rate
		
		if prev and timeToGoal > prev:
			print "Case #{0}: {1}".format(str(case + 1), str(prev))
			break

		rate += f
		time = timeToFarm
		prev = timeToGoal
