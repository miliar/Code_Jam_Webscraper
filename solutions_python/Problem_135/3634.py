#!/usr/bin/env python

# 2014 Matej Pavla
# This file is part of QaSys
 
import os, sys, getopt
import subprocess

if __name__ == '__main__': #if we run the program from command line

	file = open('input.in')

	string = file.readline()
	total_number = int(string)
	for i in range(0, total_number):
		first_row_selected = int(file.readline())
		for j in range(1, 5):
			this_line = file.readline()
			if j == first_row_selected:
				first_row = this_line.strip().split(" ")
		second_row_selected = int(file.readline())
		for j in range(1, 5):
                        this_line = file.readline()
                        if j == second_row_selected:
                                second_row = this_line.strip().split(" ")
		matches = 0
		match_num = 0
		for j in range(0, 4):
			for k in range(0, 4):
				if int(first_row[j]) == int(second_row[k]):
					match_num = int(first_row[j])
					matches += 1
		if matches == 1:
			print "Case #%d: %d" % (i+1,match_num)
		elif matches == 0:
			print "Case #%d: Volunteer cheated!" % (i+1)
		else:
			print "Case #%d: Bad magician!" % (i+1)
