#!/usr/bin/python

import sys
from operator import mul

def print_usage():
	print sys.argv[0], "<input file>", "<output file>"

def solve(A, B, p_list):
	prob_list = [float(x) for x in p_list]
	success_prob = reduce(mul, prob_list)
	com_list = []
	for i in range(A+1):
		if i == 0:
			com_list.append(success_prob)
			continue
		if i == A:
			com_list.append(1 - prob_list[0])
			continue
		com_list.append(reduce(mul, prob_list[:A-i]) * (1 - prob_list[A-i]))

	acc_list = []
	temp_sum = 0
	for elem in com_list:
		temp_sum += elem
		acc_list.append(temp_sum)

	result_list = []
	for i in range(A+1):
		stroke_type_1 = B - A + 1 + 2 * i
		stroke_type_2 = stroke_type_1 + B + 1
		result_list.append(acc_list[i] * stroke_type_1 + (1 - acc_list[i]) * stroke_type_2)

	result_list.append(B+2)

	return "%.6F" % round(min(result_list), 6)

def main():
	if len(sys.argv) != 3:
		print_usage()
		return

	in_file = open(sys.argv[1], "r")
	out_file = open(sys.argv[2], "w")

	str_list = in_file.read().split()
	in_file.close()

	count, str_list = int(str_list[0]), str_list[1:]
	for i in range(1, count + 1):
		A, B, str_list = int(str_list[0]), int(str_list[1]), str_list[2:]
		p_list, str_list = str_list[:A], str_list[A:]
		out_file.write("Case #"+str(i)+": "+solve(A, B, p_list)+"\n")

	out_file.close()

if __name__ == "__main__":
	main()
