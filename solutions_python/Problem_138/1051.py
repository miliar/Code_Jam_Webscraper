#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  code_jam_2014_qual_d.py
#  
#  Created by b00
#  

import sys

# const
test_cases = 0

blocks = {}

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
				line_num = 1
			# Read game data
			else:
				# Num of blocks
				if line_num == 1:
					line_num += 1
					continue
				# Naomi blocks
				elif line_num == 2:
					naomi_blocks = file_row.split(' ')
					blocks[test_case] = {'naomi_blocks':naomi_blocks}
					line_num += 1
				# Ken blocks
				else:
					ken_blocks = file_row.split(' ')
					blocks[test_case]['ken_blocks'] = ken_blocks
					line_num = 1
					
					test_case += 1

def convert_weights_to_float(test_case):
	tmp_weight = []
	
	for block_weight in blocks[test_case]['naomi_blocks']:
		tmp_weight.append(float(block_weight))
	
	blocks[test_case]['naomi_blocks'] = tmp_weight
	
	tmp_weight = []
	
	for block_weight in blocks[test_case]['ken_blocks']:
		tmp_weight.append(float(block_weight))
	
	blocks[test_case]['ken_blocks'] = tmp_weight

def result_of_war(test_case):
	
	# Sort blocks - optimal tactics
	naomi_blocks = sorted(blocks[test_case]['naomi_blocks'])
	ken_blocks = sorted(blocks[test_case]['ken_blocks'], reverse=True)
	
	num_of_points = 0
	
	while naomi_blocks:
		# Get naomi heaviest block
		naomi_block = naomi_blocks.pop()
		
		ken_block_best = None
		# Check if Ken has a heavier block
		for ken_block in ken_blocks:
			if ken_block > naomi_block:
				ken_block_best = ken_blocks.index(ken_block)
		
		if ken_block_best != None:
			ken_block = ken_blocks.pop(ken_block_best)
		else:
			# Get lightest block from ken blocks
			ken_block = ken_blocks.pop()
	
		# Check if naomi got point
		if naomi_block > ken_block:
			num_of_points += 1
	
	return num_of_points

def result_of_deceitful_war(test_case):
	
	# Sort blocks - optimal tactics
	naomi_blocks = sorted(blocks[test_case]['naomi_blocks'])
	ken_blocks = sorted(blocks[test_case]['ken_blocks'], reverse=True)
	
	num_of_points = 0
	
	while naomi_blocks:
		# First check if there's a block, which can't win any of fights
		# Get naomi lightest block
		naomi_lightest_block = naomi_blocks[0]
		naomi_lightest_block_can_win = False
		for ken_block in ken_blocks:
			if naomi_lightest_block > ken_block:
				naomi_lightest_block_can_win = True
		
		if not naomi_lightest_block_can_win:
			naomi_block = naomi_blocks.pop(0)
			# Get heaviest block in ken blocks
			ken_heaviest_block = ken_blocks[0]
			# Gen fake value
			# this must be used to minimize losses
			naomi_fake_block = ken_heaviest_block - 0.0000001
		else:
			# Still use naomi lightest block
			naomi_block = naomi_blocks.pop(0)
			# Get heaviest block in ken blocks
			ken_heaviest_block = ken_blocks[0]
			# but fake block weight up
			# this must be used to get correct order of fights
			naomi_fake_block = ken_heaviest_block + 0.0000001
		
		ken_block_best = None
		# Ken search for heavier block
		for ken_block in ken_blocks:
			if ken_block > naomi_fake_block:
				ken_block_best = ken_blocks.index(ken_block)
		
		if ken_block_best != None:
			ken_block = ken_blocks.pop(ken_block_best)
		else:
			# Get lightest block from ken blocks
			ken_block = ken_blocks.pop()
		
		# Check if naomi got point
		if naomi_block > ken_block:
			num_of_points += 1
	
	return num_of_points

def main():
	
	try:
		# Input file
		filename = sys.argv[1]
	except IndexError:
		print('You do not give input file!')
		return 1
	
	read_data(filename)
	
	for test_case in range(1, test_cases + 1):
		convert_weights_to_float(test_case)
		
		num_of_points_deceitful_war = result_of_deceitful_war(test_case)
		num_of_points_war = result_of_war(test_case)
		print('Case #' + str(test_case) + ': ' + str(num_of_points_deceitful_war) + ' ' + str(num_of_points_war))
	
	return 0

if __name__ == '__main__':
	main()

