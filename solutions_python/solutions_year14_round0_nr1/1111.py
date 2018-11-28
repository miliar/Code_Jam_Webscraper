#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  code_jam_2014_qual_a.py
#  
#  Created by b00
#  

import sys

test_cases = 0
# test_case:[1st_choice, 2nd_choice]
row_choice = {}
# test_case:[[first_comb], [2nd_comb]]
card_order = {}

def read_data(filename):
	
	global test_cases
	global row_choice
	global card_order
	
	with open(filename, 'r') as data_file:
		data = data_file.readlines()
		
		first_line = True
		
		test_case = 1
		card_comb = 0
		
		for file_row in data:
			file_row = file_row.strip()
			
			# Num of test cases
			if first_line:
				test_cases = int(file_row)
				first_line = False
			# Row choice
			elif (len(file_row) == 1):
				# Next / new test case
				if test_case not in row_choice.keys():
					row_choice[test_case] = []
				# 2 comb passed -> inc test_case
				elif len(row_choice[test_case]) == 2:
					test_case += 1
					card_comb = 0
					row_choice[test_case] = []
				
				row_choice[test_case].append(int(file_row))
			# Combination of lines
			elif len(file_row) > 1:
				# Next / new test case
				if test_case not in card_order.keys():
					card_order[test_case] = []
					# 1st comb
					card_order[test_case].append([])
				# 2nd comb
				elif len(card_order[test_case][0]) == 4:
					if len(card_order[test_case]) == 1:
						card_order[test_case].append([])
						card_comb = 1
				
				card_row = file_row.split(' ')
				card_order[test_case][card_comb].append(card_row)

def check_magic(test_case):
	
	first_choice = row_choice[test_case][0] - 1
	row_from_first_comb = card_order[test_case][0][first_choice]
	
	second_choice = row_choice[test_case][1] - 1
	row_from_second_comb = card_order[test_case][1][second_choice]
	
	chosen_card = None
	answer = ''
	
	# For every card in row from first comb
	for number in row_from_first_comb:
		# Check if the card is in row from second comb and we don't find choosen_card yet
		if number in row_from_second_comb and not chosen_card:
			# Write number of card
			chosen_card = number
		# Keep going - we don't find correct card yet
		elif number not in row_from_second_comb and not chosen_card:
			continue
		# Keep going - looks pretty good, we have only one card!
		elif number not in row_from_second_comb and chosen_card:
			continue
		# More than one possible card -> bad magican
		else:
			answer = 'Bad magician!'
			break
	
	# 1st possibility -> Volunteer cheated!
	if not chosen_card:
		answer = 'Volunteer cheated!'
	elif answer == '':
		answer = chosen_card
	
	return answer

def main():
	
	try:
		# Input file
		filename = sys.argv[1]
	except IndexError:
		print('You do not give input file!')
		return 1
	
	read_data(filename)
	for test_case in range(1, test_cases + 1):
		answer = check_magic(test_case)
		print('Case #' + str(test_case) + ': ' + answer)
	
	return 0

if __name__ == '__main__':
	main()

