#! /usr/bin/env python2
# -*- coding: utf-8 -*-

import sys

def parse_input(filename):
	"""
	Parse the input according to the following format

	#Test cases

	The input may of course have several test cases
	"""
	input_file = open(filename, "r")

	tc_number = int(input_file.readline())
	tc_list = []

	for i in range(tc_number):
		tc = {}
		tc['x'] = i + 1
		tc['shyness_max_level'], tc['shyness_str'] = input_file.readline().split(' ')
                tc['shyness_max_level'] = int(tc['shyness_max_level'])

		tc_list.append(tc)

	return tc_list

def standing_ovation(tc):
    required_friend = 0
    current_ovation = 0

    for s_i in range(tc['shyness_max_level'] + 1):
        required_friend += max(0, s_i - current_ovation - required_friend)
        current_ovation += int(tc['shyness_str'][s_i])

    print "Case #%i: %i" % (tc['x'], required_friend)



def main(argv):
	"""
	Our cute main function that will provide some interesting test cases to our
	sexy wizard
	"""
	filename = argv[0]
	tc_list = parse_input(filename)

	for tc in tc_list:
            standing_ovation(tc)

if __name__ == "__main__":
	main(sys.argv[1:])

