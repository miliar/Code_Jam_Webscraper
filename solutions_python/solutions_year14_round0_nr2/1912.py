"""
Overview: for each farm_cost, farm_production, and goal,
keep adding farms until you no longer are getting increasing returns
"""
file = open('cookies.txt', 'r')
file.readline()

case_count = 1

for line in file:
	farm_cost, farm_production, goal = line.split(" ")
	farm_cost = float(farm_cost)
	farm_production = float(farm_production)
	goal = float(goal)

	seconds_elapsed = 0.0
	cps = 2 # cps = "cookies per second" :)
	farms = 0

	found = False

	#import pdb; pdb.set_trace()

	while not found:
		# Compare: just waiting, or buying +1 more farm and waiting
		seconds_to_buy = farm_cost / cps
		seconds_left = goal / (cps + farm_production)
		buy = seconds_to_buy + seconds_left

		wait = goal / cps

		if (buy < wait):
			seconds_elapsed = seconds_elapsed + seconds_to_buy
			farms = farms + 1
			cps = cps + (farm_production)

		else:
			print "Case #{num}: {seconds}".format(num=case_count, seconds=wait + seconds_elapsed)
			case_count = case_count + 1
			found = True