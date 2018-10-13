#!/usr/bin/env
import sys, math

def get_file_contents():
	file_contents = open('./inputs/C-small-1-attempt3.in').read().splitlines()
	# file_contents = open('./inputs/test.txt').read().splitlines()
	return int(file_contents.pop(0)), file_contents

def loop_contents(num_lines, lines):
	for i in range(0, num_lines):
		stall_num, total_people = clean_data(lines[i])
		maximum, minimum = process_data(stall_num, total_people)
		print('Case #{0}: {1} {2}'.format(i+1, maximum, minimum))


def clean_data(line):
	arg_1, arg2 = line.split()
	return int(arg_1), int(arg2)

def process_data(stall_num, total_people):
	if stall_num == total_people:
		return 0, 0

	# occupied = 1, available = 0
	stalls = [1] + [0] * stall_num + [1]
	# stalls[math.floor(stall_num/2)]
	for person in range(0, total_people):
		maximum, minimum = update_indices(stalls)
		chosen_index = choose_stall(stalls, maximum, minimum)
	return maximum[chosen_index], minimum[chosen_index]

def choose_stall(stalls, maximum, minimum):
	max_min = max(minimum)
	available = [i for i in range(0,len(stalls)) if not stalls[i]]

	chosen_index = -1
	first_indices = [x for x in range(0, len(stalls)) if minimum[x] == max_min]
	if len(first_indices) > 1:
		max_max = max([maximum[i] for i in first_indices])
		second_indices = [i for i in first_indices if maximum[i] == max_max]
		chosen_index = second_indices[0]
	else:
		chosen_index = first_indices[0]
	stalls[chosen_index] = 1
	return chosen_index

def update_indices(stalls):
	left_index = 0
	right_index = 0
	maximum = [0] * len(stalls)
	minimum = [0] * len(stalls)
	for curr_index in range(0, len(stalls)):
		stall = stalls[curr_index]
		if not stall:
			if curr_index > right_index:
				right_index = next(i for i in range(curr_index, len(stalls)) if stalls[i])
			left = curr_index - 1 - left_index
			right = right_index - curr_index - 1
			maximum[curr_index] = max(left, right)
			minimum[curr_index] = min(left, right)
		else:
			left_index = curr_index
			maximum[curr_index] = -1
			minimum[curr_index] = -1
	return maximum, minimum


if __name__ == '__main__':
	sys.stdout=open("output.txt","w")
	num_lines, data = get_file_contents()
	loop_contents(num_lines, data)
	sys.stdout.close()