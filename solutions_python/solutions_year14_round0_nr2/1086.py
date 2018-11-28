#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  code_jam_2014_qual_b.py
#  
#  Created by b00
#  

import sys

# const
cookies_per_second = 2.0
test_cases = 0

game_params = {}

def read_data(filename):
	
	global test_cases
	
	with open(filename, 'r') as data_file:
		data = data_file.readlines()
		
		first_line = True
		
		test_case = 1
		
		for file_row in data:
			file_row = file_row.strip()
			
			# Num of test cases
			if first_line:
				test_cases = int(file_row)
				first_line = False
			# Read game data
			else:
				values = file_row.split(' ')
				game_params[test_case] = []
				# C - cost of cookie farm
				game_params[test_case].append(float(values[0]))
				# F - extra speed in cookie production
				game_params[test_case].append(float(values[1]))
				# X - cookies needed to win
				game_params[test_case].append(float(values[2]))
				
				test_case += 1

def calc_time_to_win(test_case):
	
	# We start without farm
	num_of_farms = 0
	
	# Set sum of all time needed to buy farms
	sum_of_time = 0.0
	
	while True:
		# Current time needed to win
		time_to_win = game_params[test_case][2] / (cookies_per_second + (num_of_farms * game_params[test_case][1])) + sum_of_time
		time_to_buy_farm = game_params[test_case][0] / (cookies_per_second + (num_of_farms * game_params[test_case][1]))
		
		# Sum of all time needed to buy farms
		sum_of_time += time_to_buy_farm
		
		# Assume - I bought farm
		num_of_farms += 1
		
		time_to_win_new = (game_params[test_case][2] / (cookies_per_second + (num_of_farms * game_params[test_case][1]))) + sum_of_time
		
		if time_to_win_new > time_to_win:
			return time_to_win

def main():
	
	try:
		# Input file
		filename = sys.argv[1]
	except IndexError:
		print('You do not give input file!')
		return 1
	
	read_data(filename)
	for test_case in range(1, test_cases + 1):
		time_to_win = calc_time_to_win(test_case)
		
		string = 'Case #' + str(test_case) + ': '
		print(string + '%.7f' % time_to_win)
	
	return 0

if __name__ == '__main__':
	main()

