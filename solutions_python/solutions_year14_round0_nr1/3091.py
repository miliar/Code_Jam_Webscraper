#!/usr/bin/env python
import sys

def getrow (num):
	for row in range (1, 5):
		l = sys.stdin.readline()
		if row == num:
			row1 = map (int, l.split())

	return row1



def solve (num):
	ans_1 = int (sys.stdin.readline())
	row1 = getrow (ans_1)

	ans_2 = int (sys.stdin.readline())
	row2 = getrow (ans_2)

	sol = [x for x in row1 if x in row2]

	if len (sol) == 0:
		s = "Volunteer cheated!"
	elif len (sol) > 1:
		s = "Bad magician!"
	else:
		s = str (sol[0])

	print ("Case #%d: %s" % (num, s))



num_cases = int (sys.stdin.readline())

for case in range (1, num_cases+1):
	solve (case)


