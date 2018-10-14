def farms_buy_time(farms_count, farm_cost, farm_speed):
	speed = 2.0
	time_spent = 0.0
	for i in xrange(0, farms_count):		
		time_spent += farm_cost / speed	
		speed = speed + farm_speed
	return time_spent

def solve((farm_cost, farm_speed, target)):
	min_time = -1
	farms_count = 0
	while True:
		time_to_buy_farms = farms_buy_time(farms_count, farm_cost, farm_speed)
		time_to_target_with_farms = target / (2.0 + farms_count * farm_speed)
		time_total = time_to_buy_farms + time_to_target_with_farms
		if min_time < 0:
			min_time = time_total
		else:
			if time_total < min_time:
				min_time = time_total
			else:
				return min_time
		farms_count += 1

def solve_file(filename):
	with open(filename + ".in") as f:
		lines = f.read().splitlines()

	index = 1
	with open(filename + ".out", "w") as f:
		for line in lines[1:]:
			result = solve(map(float, line.split(" ")))
			f.write("Case #{0}: {1}\n".format(index, result))
			index += 1

solve_file("B-small-attempt0")
