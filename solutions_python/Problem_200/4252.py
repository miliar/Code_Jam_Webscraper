#!/usr/bin/env python3

import sys, io

def main(fname):
	with io.open(fname, "r") as f:
		t = int(f.readline())

		for i, line in enumerate(f.readlines()):
			print("Case #{}: {}".format(i + 1, int(find_highest_tidy_num(line.strip()))))

def find_highest_tidy_num(n):
	return highest_num_helper(n, 0)

def highest_num_helper(n, index):
	if index >= len(n) - 1:
		return n

	i = tail_index(n, index + 1)

	if n[i + 1] < n[i]:
		if i == 0:
			return str(int(n[i]) - 1) + "9" * (len(n) - 1)
		n = n[:i] + str(int(n[i]) - 1) + "9" + ("" if index == 0 else n[i+2:])

	return highest_num_helper(n, index + 1)

def tail_index(string, index):
	return len(string) - 1 - index





"""
### Naive Solution - greedily counts down to next tidy number ###

def find_highest_tidy_num(n):
	while n > 0:
		if is_tidy(n):
			return n
		else:
			n -= 1
	return 0

def is_tidy(n):
	str_n = str(n)
	for i, char in enumerate(str_n):
		if i < len(str_n) - 1 and char > str_n[i + 1]:
			return False
	return True
"""

if __name__ == "__main__":
	if len(sys.argv) == 2:
		main(sys.argv[1])