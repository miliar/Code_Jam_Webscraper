#!/usr/bin/env python3

from sys import stdin

cases = int(stdin.readline())

for case in range(1, cases+1):
	candidates1 = []
	candidates2 = []

	ans1 = int(stdin.readline())
	for i in range(1, 5):
		line = stdin.readline()
		if i == ans1:
			candidates1 = [int(x) for x in line.split()]

	ans2 = int(stdin.readline())
	for i in range(1, 5):
		line = stdin.readline()
		if i == ans2:
			candidates2 = [int(x) for x in line.split()]

	result = list(set(candidates1) & set(candidates2))
	n = len(result)

	if n == 0:
		print('Case #%d: Volunteer cheated!' % (case))
	elif n == 1:
		print('Case #%d: %d' % (case, result[0]))
	else:
		print('Case #%d: Bad magician!' % (case))

