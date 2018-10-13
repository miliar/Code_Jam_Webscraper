#! /usr/bin/python3
# VIC Nicolas - Qualification Round: Problem C for the Google CodeJam 2013

import math

def is_square_and_palin(number):
	sqrt = math.sqrt(float(number))
	trunc = math.trunc(sqrt)
	if (sqrt - trunc) > 0.0000000001 :
		return 0

	if is_palindrome(trunc):
		return 1
	else:
		return 0

def is_palindrome(number_string):
	number_string = str(number_string)
	for i in range(math.ceil(len(number_string) / 2)):
		if number_string[i] != number_string[len(number_string) - i - 1]:
			return 0
	return 1

counter = 1
def print_case(string):
	global counter
	print("Case #{}: {}".format(counter, string))
	counter = counter + 1
		
total_numbers = input()
for i in range(int(total_numbers)):
	input_range = input().split()
	number_count = 0
	for i in range(int(input_range[0]), int(input_range[1]) + 1):
		if is_palindrome(i) and is_square_and_palin(i):
			number_count = number_count + 1
	print_case(number_count)

