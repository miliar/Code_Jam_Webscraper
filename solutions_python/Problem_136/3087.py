#! /usr/bin/python3

import sys;

input_filename = sys.argv[1];
output_filename = input_filename + ".out";

file_in = open(input_filename, "r");
file_out = open(output_filename, "w");

T = int(file_in.readline());
for t in range(T):
	""" read input """
	inputs = file_in.readline().split();
	C = float(inputs[0])
	F = float(inputs[1])
	X = float(inputs[2])

	""" print output """

	result = 0.0

	rate = 2
	while True:
		cur_win_time = X / rate
		cur_buy_time = C / rate
		next_rate = rate + F
		next_win_time = X / next_rate
		if next_win_time + cur_buy_time < cur_win_time:
			result += cur_buy_time
			rate = next_rate
		else:
			result += cur_win_time
			break;



	file_out.write("Case #%d: %.7f\n" % (t+1, result))

file_in.close();
file_out.close();