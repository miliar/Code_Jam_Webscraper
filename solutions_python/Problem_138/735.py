#!/usr/bin/env python

import sys
import re

total_tests = 0
test_counter = 1
ctr = 0
number_of_block = 0
naomi_blocks1 = []
naomi_blocks2 = []
ken_blocks1 = []
ken_blocks2 = []

for line in sys.stdin:
	if ctr == 0:
		total_tests = int(line)
	if ctr == 1:
		number_of_block = int(line)
	if ctr == 2:
		for num in  re.findall("\d+.\d+", line):
			naomi_blocks1.append(float(num))
		naomi_blocks1 = sorted(naomi_blocks1)
		naomi_blocks2 = naomi_blocks1[:]
	if ctr == 3:
		for num in  re.findall("\d+.\d+", line):
			ken_blocks1.append(float(num))
		ken_blocks1 = sorted(ken_blocks1)
		ken_blocks2 = ken_blocks1[:]
		
		deceitful_num = 0
		for x in range(0,number_of_block): 
			if naomi_blocks1[0] < ken_blocks1[0]:
				del naomi_blocks1[0]
				del ken_blocks1[len(ken_blocks1)-1]
			else:
				del naomi_blocks1[0]
				del ken_blocks1[0]
				deceitful_num = deceitful_num + 1
		
		original_counter = False
		original_num = 0
		break_counter = 0
		for x in range(0,number_of_block):
			original_counter = False
			for y in range(break_counter,number_of_block):
				if naomi_blocks2[x] < ken_blocks2[y]:
					original_counter = True
					break_counter = y+1
					break
			if original_counter == False:
				original_num = original_num + 1

		sys.stdout.write("Case #" + str(test_counter) + ": ")
		sys.stdout.write(str(deceitful_num)+ " ")
		sys.stdout.write(str(original_num)+ "\n")

		test_counter = test_counter + 1
		number_of_block = 0
		naomi_blocks1 = []
		naomi_blocks2 = []
		ken_blocks1 = []
		ken_blocks2 = []
		ctr = 1
		continue
		

	ctr = ctr+1
