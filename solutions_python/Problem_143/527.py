#!/usr/bin/env python
import sys

input_file_name = 'B-small-attempt0.in'

with open(input_file_name, 'r') as file_in:
	with open('result_{}'.format(input_file_name), 'w') as file_out:
		test_case_size = int(file_in.readline())
		test_case_number = 0
		while test_case_number < test_case_size:
			answer = 0
			test_case_number += 1
			
			a, b, k = [int(x) for x in file_in.readline().split(' ')]

			if a > k:
				answer += k * (b)
				aa = range(k, a)
			else:
				aa = range(0, a)
			bb = range(0, b)

			for x in aa:
				for y in bb:
					if x & y < k:
						answer += 1

			file_out.write('Case #{}: {}'.format(test_case_number, answer))
			if test_case_number < test_case_size:
				file_out.write('\n')


