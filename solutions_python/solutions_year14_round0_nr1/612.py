#!/usr/bin/env python

with open('A-small-attempt2.in', 'r') as f:
	with open('output.txt', 'w') as out:
		row_index = [1, 2, 3, 4]

		test_case_size = int(f.readline())
		test_case_number = 0
		while test_case_number < test_case_size:
			test_case_number += 1
			first_position = int(f.readline())
			for index in row_index:
				if first_position == index:
					first_set = set(f.readline().strip().split(' '))
				else:
					f.readline()
			second_position = int(f.readline())
			for index in row_index:
				if second_position == index:
					second_set = set(f.readline().strip().split(' '))
				else:
					f.readline()
			intersection_result = first_set.intersection(second_set)
			intersection_count = len(intersection_result)

			if intersection_count == 0:
				out.write('Case #{}: Volunteer cheated!\n'.format(test_case_number))
			elif intersection_count == 1:
				out.write('Case #{}: {}\n'.format(test_case_number, intersection_result.pop()))
			else:
				out.write('Case #{}: Bad magician!'.format(test_case_number))
				if test_case_number < test_case_size:
					out.write('\n')