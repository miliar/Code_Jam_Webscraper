#!/usr/bin/python

import os,sys

f = open(sys.argv[1], 'r')

def solve(row1, rows1, row2, rows2):
	result = set(rows1[row1]).intersection(set(rows2[row2]))
	if len(result) == 0:
		return "Volunteer cheated!"
	if len(result) > 1:
		return "Bad magician!"
	return result.pop()

for t in range(int(f.readline())):
	row1 = int(f.readline()) -1
	rows1 = []
	for _ in range(4):
		rows1.append(f.readline().strip().split(' '))

	row2 = int(f.readline()) -1
	rows2 = []
	for _ in range(4):
		rows2.append(f.readline().strip().split(' '))

	print "Case #%d: %s" % (t+1, solve(row1, rows1, row2, rows2))
