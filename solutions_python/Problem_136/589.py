#!/usr/bin/env python
import sys

c = 0
f = 0
x = 0

def calculate():
	last_result = sys.float_info.max
	current_result = 0
	rate = 2

	while current_result <= last_result:
		time_for_wait = x / rate + current_result
		if time_for_wait >= last_result:
			return last_result
		last_result = time_for_wait
		time_for_next_farm = c / rate + current_result
		if time_for_next_farm < last_result:
			current_result = time_for_next_farm
			rate = rate + f
		else:
			return last_result
	return last_result


with open('B-large.in', 'r') as file_in:
	with open('output.txt', 'w') as file_out:
		test_case_size = int(file_in.readline())
		test_case_number = 0
		while test_case_number < test_case_size:
			test_case_number += 1
			c, f, x = [float(x) for x in file_in.readline().split(' ')]
			file_out.write('Case #{}: {}'.format(test_case_number, "{0:.7f}".format(calculate())))
			if test_case_number < test_case_size:
				file_out.write('\n')

			