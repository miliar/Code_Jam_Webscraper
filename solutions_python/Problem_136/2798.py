#! /usr/bin/python3

import sys

def find_cookie_time2(c, r, dr, x):
	t = 0
	while x / float(r) > c / float(r) + x / float(r + dr):
		t += c / float(r)
		r += dr
	return t + x / float(r)

with open(sys.argv[1]) as test_file:
	lines = [line.strip() for line in test_file.readlines()]
	num_tests = int(lines[0])
	i = 1
	for test in [list(map(lambda x: float(x), line.split())) for line in lines[1:len(lines)]]:
		total_time = find_cookie_time2(test[0], 2, test[1], test[2])
		print('Case #{}: {}'.format(i, '%.7f' % total_time))
		i += 1
