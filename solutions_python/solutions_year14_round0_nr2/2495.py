#!/usr/bin/env python
import sys


def compute(c, f, x):
	time = 0.0
	rate = 2
	while True:
		time_to_win = x / rate
		time_to_factory = c / rate + x /(rate + f)
		if time_to_win <= time_to_factory:
			# keep going
			# print 'win'
			return time + time_to_win
		else:
			# build factory
			# print '> build factory after', c/rate
			time += c / rate
			rate += f



def parse_input(stream):
	test_cases_to_expect = int(stream.readline())
	for _ in xrange(test_cases_to_expect):
		yield map(float, stream.readline().split(' '))


if __name__ == '__main__':
	for n, test_case in enumerate(parse_input(sys.stdin), start=1):
		c, f, x = test_case
		y = compute(c, f, x)
		print 'Case #{}: {}'.format(n, y)

