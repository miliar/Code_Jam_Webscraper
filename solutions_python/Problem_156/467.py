# -*- coding: utf-8 -*-

MAX_PANCAKE_NUM = 2100

def calc_min_time(P):
	# set up diner_num
	diner_num = [0] * MAX_PANCAKE_NUM
	max_pancake = 0
	for x in P:
		diner_num[x] += 1
		max_pancake = max(max_pancake, x)


	min_time = max_pancake
	for i in reversed(range(2, max_pancake)):
		min_time = min(min_time, i + min_split_time_with_max_pancake(diner_num, i))

	return min_time

def min_split_time_with_max_pancake(diner_num, max_pancake):
	split_time = 0
	for i in reversed(range(max_pancake + 1, MAX_PANCAKE_NUM)):
		if diner_num[i] == 0:
			continue
		split_time += diner_num[i] * ((i-1) / max_pancake)
	return split_time


def main():
	input_file = 'B-large.in.txt'
	output_file = 'out'
	output_format = 'Case #{0}: {1}\n'

	results = []

	with open(input_file, 'r') as f:
		case_total = str_to_int(f.readline())
		# for each case:
		for i in range(case_total):
			# some code . reading
			D = str_to_int(f.readline())
			P = str_to_int_list(f.readline())
			results.append(calc_min_time(P))

	with open(output_file, 'w') as f:
		for i in range(len(results)):
			# for each result
			f.write(output_format.format(i+1, results[i]))	


# --------------------------------------------

def str_to_int(s):
	return int(s.strip())

def str_to_int_list(s):
	return [int(x) for x in s.strip().split()]

if __name__ == '__main__':
	main()



