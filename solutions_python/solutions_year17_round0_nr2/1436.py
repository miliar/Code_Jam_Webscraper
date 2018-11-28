from __future__ import print_function
import sys
import time

def read_file(fn):
	with open(fn) as f:
		cont = f.readlines()
	print("Read input file \"" + fn + "\" successfully!")	
	return [line.strip().split(" ")  for line in cont]

def handle_input(fc, out_name):
	output_file = open(out_name, 'w')
	print("Opened output file \"" + out_name + "\" successfully!")
	test_cases_count = int(fc[0][0])
	
	for test_index in range(1, test_cases_count + 1):
		print("Case #" + str(test_index) + "... ", end = '')
		result = handle_line(fc[test_index])
		output_file.write("Case #" + str(test_index) + ": " + result + "\n")
		print("Done")
	output_file.close()
	return

def handle_line(line):
	init_num = line[0]
	res_num = ""
	max_digit = 0
	for index in range(len(init_num)):
		dig = init_num[index]
		if ord(dig) >= max_digit:
			max_digit = ord(dig)
			res_num += dig
		else:
			len_left = len(init_num) - index
			return str(int(recreate(res_num) + "9" * len_left))
	return str(int(res_num))

def recreate(num):
	num = "0" + num
	for dig_index in range(len(num) - 1, 0, -1):
		if ord(num[dig_index]) > ord(num[dig_index - 1]):
			return num[:dig_index] + chr(ord(num[dig_index]) - 1) + \
			"9" * (len(num) - (dig_index + 1))
	return "NULL"

def replace(string, index, new_char):
	return string[:index-1] + new_char + string[index:]	

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Not enough args!")
	else:
		input_name = sys.argv[1]
		file_cont = read_file(input_name)	

		output_name = input_name[:input_name.index(".")] + ".out"
		handle_input(file_cont, output_name)	

