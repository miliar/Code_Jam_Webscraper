#!/usr/bin/env python
import sys

with open('D-large.in', 'r') as file_in:
	with open('output.txt', 'w') as file_out:
		test_case_size = int(file_in.readline())
		test_case_number = 0
		while test_case_number < test_case_size:
			test_case_number += 1
			
			length = int(file_in.readline())
			naomi_blocks = [float(x) for x in file_in.readline().split(' ')]
			ken_blocks = [float(x) for x in file_in.readline().split(' ')]
			naomi_blocks.sort()
			ken_blocks.sort()

			ken_points = 0
			index = 0
			for block in ken_blocks:
				if block > naomi_blocks[index]:
					ken_points += 1
					index += 1

			naomi_blocks = naomi_blocks
			ken_blocks = ken_blocks

			index_start = 0
			len_start = len(ken_blocks)
			naomi_points = 0
			while len_start > 0:
				temp_result = 0
				for x in range(len_start):
					if naomi_blocks[index_start + x] > ken_blocks[x]:
						temp_result += 1
				naomi_points = max(naomi_points, temp_result)
				index_start += 1
				len_start -= 1

			war_points = length - ken_points
			deceitful_points = naomi_points

			file_out.write('Case #{}: {} {}'.format(test_case_number, deceitful_points, war_points))
			if test_case_number < test_case_size:
				file_out.write('\n')

			