#! /usr/bin/env python2
# -*- coding: utf-8 -*-

import sys

def parse_input(filename):
	"""
	Parse the input according to the following format

	#Test cases
	#Answer to the first arrangement
	#First Arrangement 4x4
	#Answer to the second arrangement
	#Second Arrangement 4x4

	The input may of course have several test cases
	"""
	input_file = open(filename, "r")

	tc_number = int(input_file.readline())
	tc_list = []

	for i in range(tc_number):
		tc = {}
		tc['x'] = i + 1
		tc['first_row']  = int(input_file.readline()) - 1
		tc['first_arr']  = [[int(x) for x in input_file.readline().split(' ')]
				for n in range(4)]
		tc['second_row'] = int(input_file.readline()) - 1
		tc['second_arr'] = [[int(x) for x in input_file.readline().split(' ')]
				for n in range(4)]

		tc_list.append(tc)

	return tc_list

def sexy_wizard(tc):
	"""
	Sexy wizard is the best and sexiest wizard in this git repository so be
	aware
	"""
	y = 0
	result = set(tc.get('first_arr')[tc.get('first_row')]).intersection(
			tc.get('second_arr')[tc.get('second_row')])

	try:
		y = result.pop()

		if len(result):
			print "Case #%i: Bad magician!" % tc.get('x')
		else:
			print "Case #%i: %i" % (tc.get('x'), y)

	except KeyError:
		print "Case #%i: Volunteer cheated!" % tc.get('x')

def main(argv):
	"""
	Our cute main function that will provide some interesting test cases to our
	sexy wizard
	"""
	filename = argv[0]
	tc_list = parse_input(filename)

	for tc in tc_list:
		sexy_wizard(tc)

if __name__ == "__main__":
	main(sys.argv[1:])
