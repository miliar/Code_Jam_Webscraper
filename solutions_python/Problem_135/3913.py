#!/usr/bin/env python

from sys import stdin
from sets import Set

for case in range(int(stdin.readline())):
	rows = [ Set(), Set() ]
	for question in range(2):
		answer = int(stdin.readline())
		for row in range(1, 5):
			if row == answer:
				for item in (stdin.readline().split()):
					rows[question].add(item)
			else:
					stdin.readline()
	result = rows[0] & rows[1]

	if len(result) == 1:
		output = str(result.pop())
	elif len(result) == 0:
		output = 'Volunteer cheated!'
	elif len(result) > 1:
		output = 'Bad magician!'

	print 'Case #' + str(case + 1) + ': ' + output
