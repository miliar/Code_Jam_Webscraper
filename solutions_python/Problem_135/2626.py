#!/usr/bin/python

# B. Cookie clicker

import sys



f = sys.stdin
T = int(f.readline())

for t in range(1, T+1):
	print "Case #%d:" % t,

	row1 = int(f.readline().strip())

	matrix1 = []
	for i in range(4):
		matrix1.append(map(int, f.readline().strip().split()))

	row2 = int(f.readline().strip())

	matrix2 = []
	for i in range(4):
		matrix2.append(map(int, f.readline().strip().split()))

	count = 0
	for elem in matrix1[row1 - 1]:
		if elem in matrix2[row2 - 1]:
			count += 1
			answer = elem

	if count == 0:
		print "Volunteer cheated!"
	elif count == 1:
		print answer
	else:
		print "Bad magician!"
