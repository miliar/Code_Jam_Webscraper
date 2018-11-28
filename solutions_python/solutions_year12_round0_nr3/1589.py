#! /usr/bin/env python
from sys import stdin

def get_input():
	data = stdin.readlines()
	for x in range(0, len(data)):
		data[x] = data[x].replace("\n", "")
	return data

def left_shift(num_string):
	array = list(num_string)
	bucket = array[0]
	for x in range(1, len(array)):
		array[x-1] = array[x]
	array[-1] = bucket
	return str(''.join(array))

def get_mods(num):
	bucket = []
	tmp = str(num)
	while(1):
		bucket.append(tmp)
		tmp = left_shift(tmp)
		if tmp == str(num):
			break
	return bucket

def find_pairs(a, b):
	num = 0
	for x in range(a, b + 1):
		for y in get_mods(x):
			if int(y) > x and int(y) < b + 1:
				num += 1
	return num

def main():
	input_data = get_input()
	num_cases = input_data[0]
	for x in range(1, len(input_data)):
		input_data[x] = input_data[x].split()
		print "Case #%d: %d" % (x, find_pairs(int(input_data[x][0]), int(input_data[x][1])))

if __name__ == "__main__":
	main()
