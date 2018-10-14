#!/usr/bin/python
import sys

f = open(sys.argv[1], 'r')
inputs = f.read()
f2 = open("large_output", 'w')

lines = inputs.split('\n')
total_cases = lines[0]
for case in range(int(total_cases)):
	inputs = lines[case+1].split(" ")
	farm_cost = float(inputs[0])
	farm_rate = float(inputs[1])
	win_cond = float(inputs[2])

	total_time = 0
	farm_count = 0

	while True:
		current_rate = farm_count * farm_rate + 2
		time2farm = farm_cost / current_rate
		time2farmwin = time2farm + win_cond / (current_rate + farm_rate)
		time2win = win_cond / current_rate

		if time2farmwin > time2win:
			total_time += time2win
			break

		total_time += time2farm
		farm_count += 1

	f2.write("Case #%i: %0.7f\n" % (case+1, total_time))