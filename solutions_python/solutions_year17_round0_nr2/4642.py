#!/usr/bin/env
import sys

def get_file_contents():
	file_contents = open('./inputs/B-small-attempt1.in').read().splitlines()
	return int(file_contents.pop(0)), file_contents

def loop_contents(num_lines, lines):
	for i in range(0, num_lines):
		process_num = lines[i]
		answer = process_data(process_num)
		print('Case #{0}: {1}'.format(i+1, answer))


def process_data(num):
	current_num = num
	while is_dirty(current_num):
		current_num = str(int(current_num) - 1)
	return current_num


def is_dirty(orig):
	if len(orig) == 1:
		return False

	digits = list(orig)
	digits.sort()

	if ''.join(digits) == orig:
		return False

	return True


if __name__ == '__main__':
	sys.stdout=open("output.txt","w")
	num_lines, data = get_file_contents()
	loop_contents(num_lines, data)
	sys.stdout.close()