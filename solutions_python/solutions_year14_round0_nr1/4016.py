#!/usr/bin/env python
from __future__ import division
import sys
import argparse
from collections import defaultdict

def main():
	num_cases = int(sys.stdin.readline().strip())
	for num_case in range(num_cases):
		row1 = sys.stdin.readline().strip()
		buffer = ''.join(sys.stdin.readline() for i in range(4))
		board1 = []
		for row in buffer.strip().split('\n'):
			row = row.strip().split(' ')
			row = [int(num) for num in row]
			board1.append(row)
			
		row2 = sys.stdin.readline().strip()
		buffer = ''.join(sys.stdin.readline() for i in range(4))
		board2 = []
		for row in buffer.strip().split('\n'):
			row = row.strip().split(' ')
			row = [int(num) for num in row]
			board2.append(row)
		
		
		magic = find_card(row1, row2, board1, board2)
		if magic == "2":
			print "Case #{}: Bad magician!".format(num_case+1)
		elif magic == "3": 
			print "Case #{}: Volunteer cheated!".format(num_case+1)
		else:
			print "Case #{}: {}".format(num_case+1, magic)

def find_card(row1, row2, board1, board2):
	candidates = set(int(t) for t in board1[int(row1)-1])
	magic = "S"
	for candidate in board2[int(row2)-1]:
		candidate = int(candidate)
		if candidate in candidates:
			if magic == "S":
				magic = candidate
			else:
				return "2"
	if magic == "S":
		return "3"
	else:
		return magic

main()