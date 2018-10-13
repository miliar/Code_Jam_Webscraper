#!/usr/bin/env python

import sys

total_tests = 0
test_counter = 1
ctr = 0
row_num1 = 0
row_num2 = 0
square1 = []
square2 = []

for line in sys.stdin:
	if ctr == 0:
		total_tests = int(line)
	if ctr == 1:
		row_num1 = int(line)
	if ctr > 1 and ctr < 6:
		row = [int(s) for s in line.split() if s.isdigit()]
		square1.append(row)
	if ctr == 6:
		row_num2 = int(line)
	if ctr > 6 and ctr < 11:
		row = [int(s) for s in line.split() if s.isdigit()]
		square2.append(row)
	if ctr == 10:
		num_share = 0
		share_number = 0
		for num1 in square1[row_num1-1]:
			for num2 in square2[row_num2-1]:
				if num1 == num2:
					num_share = num_share+1
					share_number = num1
					break
		sys.stdout.write("Case #"+str(test_counter)+": ")
		if num_share == 1:
			sys.stdout.write(str(share_number)+"\n")
		elif num_share > 1:
			sys.stdout.write("Bad magician!\n")
		elif num_share == 0:
			sys.stdout.write("Volunteer cheated!\n")

		test_counter = test_counter+1
		total_tests = total_tests-1
		if total_tests == 0:
			break
		ctr = 1
		row_num1 = 0
		row_num2 = 0
		square1 = []
		square2 = []
		continue
		#calculate
	ctr = ctr + 1

