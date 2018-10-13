#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

input = sys.stdin.readlines()
cases = int(input[0])

for i in range(0, cases):
	offset = 1 + i*10
	row_num = int(input[offset])
	row = set(map(int, input[offset+row_num].split()))

	offset += 5
	row_num2 = int(input[offset])
	row2 = set(map(int, input[offset+row_num2].split()))

	print "Case #" + str(i+1) + ":",
	intersect = row.intersection(row2)
	
	if(len(intersect) < 1):
		print "Volunteer cheated!"
	elif(len(intersect) == 1):
		print intersect.pop()
	elif(len(intersect) > 1):
		print "Bad magician!"