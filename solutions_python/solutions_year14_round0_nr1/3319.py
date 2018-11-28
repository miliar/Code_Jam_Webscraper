#!/usr/bin/python

import sys

def xth_row(x):
	for i in range(4):
		if i == x - 1:
			ret = input()
		else:
			input()
	return set([int(num) for num in ret.split()])

for i in range(int(input())):
	i += 1
	j_ = int(input())
	j_row = xth_row(j_)
	k_ = int(input())
	k_row = xth_row(k_)
	possible = tuple(k_row & j_row)
	if len(possible) == 1:
		print("Case #%d: %s" % (i, possible[0]))
	elif len(possible) > 1:
		print("Case #%d: %s" % (i, "Bad magician!"))
	elif len(possible) == 0:
		print("Case #%d: %s" % (i, "Volunteer cheated!"))
