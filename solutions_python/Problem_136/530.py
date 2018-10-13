#! /usr/bin/env python2
# -*- coding: utf-8 -*-

import sys

def parse_input(filename):
	"""
	Parse the input according to the following format:

	The first line of the input gives the number of test cases, T. T lines
	follow. Each line contains three space-separated real-valued numbers: C, F
	and X, whose meanings are described earlier in the problem statement.

	C, F and X will each consist of at least 1 digit followed by 1 decimal point
	followed by from 1 to 5 digits. There will be no leading zeroes.
	"""
	input_file = open(filename, "r")

	tc_number = int(input_file.readline())
	tc_list = []

	for i in range(tc_number):
		C, F, X = [float(x) for x in input_file.readline().split(' ')]
		tc = {'x': i + 1, 'C': C, 'F': F, 'X': X}
		tc_list.append(tc)

	return tc_list

def click_click(tc):
	"""
	Compute the necessary time in order to reach the aimed number of cookies
	"""
	cookies_per_second = 2

	C, F, X = tc.get('C'), tc.get('F'), tc.get('X')

	time = float("inf")
	improved_time = X / cookies_per_second
	farm_time = 0

	while improved_time < time:
		#time cost for one farm
		farm_time += C / cookies_per_second
		cookies_per_second += F
		time = improved_time
		improved_time = farm_time + X / cookies_per_second

	print "Case #%i: %.7f" % (tc.get('x'), time)

def main(argv):
	"""
	You thought that our wizard went to sleep after the previous act? It seems
	you are wrong to see how he is trying as hard as possible to rule the world
	through the cookies market. So let's help him, maybe one day he will reward
	us quite greatly. Mwahahahahaha!!!
	"""
	filename = argv[0]
	tc_list = parse_input(filename)

	for tc in tc_list:
		click_click(tc)

if __name__ == "__main__":
	main(sys.argv[1:])
