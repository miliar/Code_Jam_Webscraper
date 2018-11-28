#!/usr/bin/env python

def read_input():
	num_test_cases = input()
	test_cases = []
	for i in range(0, num_test_cases):
		c, f, x = tuple(map(float, raw_input().split()))
		test_cases.append((c, f, x))
	return test_cases

def process_test_case(c, f, x):
	t = 0.0
	cps = 2.0

	while True:
		t_until_x = x / cps
		t_until_c = c / cps
		t_until_x_after_c = x / (cps + f)

		if t_until_x < t_until_c + t_until_x_after_c:
			return t + t_until_x
		else:
			t += t_until_c
			cps += f

	return t

def process_all_test_cases(test_cases):
	for i, test_case in enumerate(test_cases):
		print "Case #{}: {}".format(i + 1, process_test_case(*test_case))

if __name__ == "__main__":
	process_all_test_cases(read_input())