#!/usr/bin/env python
import sys

input_file_name = 'A-small-attempt0.in'

def extract_word(word):
	result = []
	index = None
	current_string = None
	for x in word:
		if current_string == None:
			current_string = x
		else:
			if current_string[-1] == x:
				current_string += x
			else:
				result.append(current_string)
				current_string = x
	if current_string:
		result.append(current_string)
	return [(x[0], len(x)) for x in result]

def calculate_min_diff(count_list):
	total_value = sum(count_list)
	interval_count = len(count_list)
	diff = total_value
	current_pivot = interval_count
	pivot_answer = current_pivot
	while(True):
		next_diff = abs(total_value - current_pivot)
		if next_diff < diff:
			diff = next_diff
			pivot_answer = current_pivot
			current_pivot += interval_count
		else:
			break
	pivot_answer /= interval_count
	return sum([abs(x-pivot_answer) for x in count_list])

with open(input_file_name, 'r') as file_in:
	with open('result_{}'.format(input_file_name), 'w') as file_out:
		test_case_size = int(file_in.readline())
		test_case_number = 0
		while test_case_number < test_case_size:
			answer = None
			test_case_number += 1
			
			word_count = int(file_in.readline())
			word_list = []

			for x in range(word_count):
				word_list.append(extract_word(file_in.readline().strip()))

			# check the length
			uniq_char_count = len(word_list[0])
			length_list = [len(x) for x in word_list]
			if all(x == uniq_char_count for x in length_list):
				# check the character
				character_check = True
				for x in range(uniq_char_count):
					char_set = set()
					for y in word_list:
						char_set.add(y[x][0])
					if len(char_set) > 1:
						character_check = False
						break
				if character_check:
					answer = answer or 0
					for x in range(uniq_char_count):
						count_list = []
						for y in word_list:
							count_list.append(y[x][1])
						answer += calculate_min_diff(count_list)

			file_out.write('Case #{}: {}'.format(test_case_number, answer if answer != None else 'Fegla Won'))
			if test_case_number < test_case_size:
				file_out.write('\n')


