#! /usr/bin/env python

import os, sys, inspect
# realpath() with make your script run, even if you symlink it :)
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
if cmd_folder not in sys.path:
	sys.path.insert(0, cmd_folder)

import math


def is_palindrome(num):
    return str(num) == str(num)[::-1]

def gen_palindromes(number_length, A, B):
	start = 0
	end_str = '9'
	for i in range(number_length/2-1):
		end_str += '9'
	end = int(end_str)

	palindromes = list()
	# print '\tnumber_length = %d, start = %d, end = %d' % (number_length, start, end+1)
	for i in range(start, end+1):
		first_half = str(i)
		second_half = first_half[::-1]
		if(2*len(first_half) < number_length):
			for i in range(10):
				middle = str(i)
				palindrome = int(first_half+middle+second_half)
				if(palindrome >= A and palindrome <= B):
					palindromes.append(palindrome)
		elif(2*len(first_half) > number_length):
			palindrome = int(first_half)
			if(palindrome >= A and palindrome <= B):
				palindromes.append(palindrome)
		else:
			palindrome = int(first_half+second_half)
			if(palindrome >= A and palindrome <= B):
				palindromes.append(palindrome)

	return palindromes

def find_fair_squares(A, B):
	# palindromes = gen_palindromes(A, B)

	sqrt_A = int(math.sqrt(A))
	sqrt_B = int(math.sqrt(B)+1)
	shortest_number = len(str(sqrt_A))
	longest_number = len(str(sqrt_B))

	print A, B, sqrt_A, sqrt_B, shortest_number, longest_number

	num_fair_squares = 0
	for num_len in range(shortest_number, longest_number+1):
		palindromes = gen_palindromes(num_len, sqrt_A, sqrt_B)
		for palindrome in palindromes:
			test_num = palindrome*palindrome

			# sanity check
			# print '\tsqrt_test_num = %d, test_num = %d' % (palindrome, test_num)
			if(test_num < A or test_num > B):
				# print '\t[Warning] %d is out of range' % test_num
				continue

			if(is_palindrome(test_num)):
				num_fair_squares += 1

	return num_fair_squares


def main(argv):
	in_file_path = argv[1]
	in_file = open(in_file_path, 'rb')

	out_file_path = '%s.out' % in_file_path
	out_file = open(out_file_path, 'wb')

	T = int(in_file.readline())
	for case_num in range(T):
		params = in_file.readline().split()
		A = int(params[0].strip())
		B = int(params[1].strip())

		num_fair_squares = find_fair_squares(A, B)
		out_file.write('Case #%d: %d\n' % (case_num+1, num_fair_squares))


if(__name__ == '__main__'):
	ret = main(sys.argv)
	sys.exit(ret)

