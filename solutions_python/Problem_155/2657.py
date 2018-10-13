#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  a.py
#  
#  Copyright 2015 b00
#  
#  

import fileinput

def calc_friends(audience, s_max):
	friends_counter = 0
	
	curr_counted_people = 0
	for s_lvl, c_p in sorted(audience.items()):
		if curr_counted_people >= s_lvl:
			curr_counted_people += c_p
			if curr_counted_people >= int(s_max):
				return friends_counter
			else:
				continue
		else:
			how_many_friends = s_lvl - curr_counted_people
			friends_counter += how_many_friends
			curr_counted_people = curr_counted_people + how_many_friends + c_p
			if curr_counted_people >= int(s_max):
				return friends_counter
			else:
				continue	

def main():
	
	curr_t_case = 1
	first_line = True
	for line in fileinput.input():
			line = line.strip()
			
			if first_line:
				t_cases = int(line)
				first_line = False
				continue
			
			s_max, s_audience = line.split(' ')
			audience = {}
			
			if int(s_max) == 0:
				print('Case #', curr_t_case ,': ', 0, sep='')
				curr_t_case += 1
				continue
			else:
				curr_s_lvl = 0
				for s_l in s_audience:
					# shyness level = how many people
					audience[curr_s_lvl] = int(s_l)
					curr_s_lvl += 1
				
			friends_counter = calc_friends(audience, s_max)
			
			print('Case #', curr_t_case ,': ', friends_counter, sep='')
			curr_t_case += 1
	
	return 0

if __name__ == '__main__':
	main()
