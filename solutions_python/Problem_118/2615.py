def is_palindrome(num):	
	num_str = str(num)
	return num_str == num_str[::-1]


def find_numbers(min, max):
	import math
	numbers = []
	for i in range (min, max+1):
		(a, b) = i, math.sqrt(i)	
		if b % 1 == 0:
			if is_palindrome(a) and is_palindrome(int(b)):
				numbers.append(i)
	return numbers


def process_input(lines):	
	number_of_cases = int(lines[0].strip())
	cases = []	
	for i in range(0, number_of_cases):
		cases.append(lines[i+1].strip())
		
	return cases


def main():
	import os, sys
	f = open(sys.argv[1])
	input = f.readlines()
	output = open(sys.argv[2], 'w')
	
	cases = process_input(input)
	i = 1
	for case in cases:
		(min, max) = case.split(' ')
		nums = len(find_numbers(int(min), int(max)))
		outstr = "Case #" + str(i) + ": " + str(nums)		
		output.write(outstr + "\n")
		i += 1
		print outstr

if __name__ == "__main__":
    main()