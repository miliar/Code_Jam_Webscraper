#!/bin/python



def CalcOneDay(max_runs, max_passengers, groups):
	num_groups = len(groups)
	
	def CalcOneRun(starting_group_index):
		num_passengers = 0
		next_group_index = starting_group_index
		while True:
			group_size = groups[next_group_index]
			if num_passengers + group_size > max_passengers: break
			num_passengers += group_size
			next_group_index = (next_group_index + 1) % num_groups
			if next_group_index == starting_group_index: break
		return (next_group_index, num_passengers)
			
	history_for_group = [None] * num_groups
	
	profits = 0
	run_index = 0
	group_index = 0
	
	while run_index < max_runs:
		# Check history for a cycle
		if history_for_group[group_index]:
			# If found cycle, pump it
			# print "Found cycle on run", run_index, "with group", group_index, ":", history_for_group
			previous_run_index, previous_profits = history_for_group[group_index]
			cycle_length = run_index - previous_run_index
			cycle_profits = profits - previous_profits
			num_cycles = int((max_runs - run_index) / cycle_length)
			# print "Running cycle %d times for %d*%d profit" % (num_cycles, cycle_length, cycle_profits)
			profits += num_cycles * cycle_profits
			history_for_group = [None] * num_groups
			run_index += num_cycles * cycle_length
		else:
			# Save history for this state
			history_for_group[group_index] = (run_index, profits)
			next_group_index, num_passengers = CalcOneRun(group_index)
			group_index = next_group_index
			profits += num_passengers
			run_index += 1
	
	return profits
		

if __name__ == '__main__':
	for case_number in xrange(1, int(raw_input())+1):
		max_runs, max_passengers, num_groups = map(int, raw_input().split())
		groups = map(int, raw_input().split())
		income = CalcOneDay(max_runs, max_passengers, groups)
		print "Case #%d: %s" % (case_number, str(income))

	
	
	