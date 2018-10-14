import sys, math

cases = int(sys.stdin.readline().rstrip())

for case in range(cases):

	inputs = map(float, sys.stdin.readline().rstrip().split())

	farm_cost = inputs[0]
	farm_output = inputs[1]
	end_game = inputs[2]

	# Calculate the base total time (no farms)
	base_total = end_game / 2

	# Now consider farms
	num_farms = 0
	best_time = base_total

	while True:

		total_time = 0

		for i in range(num_farms):

			# Time it takes to get to each consecutive farm
			total_time += farm_cost / (2 + i * farm_output)

		# Get the total time to get the target from the new output
		total_time += (end_game / (2 + num_farms * farm_output))

		if total_time <= best_time:

			best_time = total_time

			num_farms += 1

		else:

			print 'Case #' + str(case+1) + ': ' + str(best_time)

			break