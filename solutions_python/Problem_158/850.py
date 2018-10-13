from __future__ import division
from cjlib.input import *
from cjlib.runner import TaskRunner, MPQRunner, DummyRunner
from itertools import permutations
import math

get("""4
2 2 2
2 1 3
4 4 1
3 2 3
3 3 3
4 2 2
4 4 2
2 3 3
4 2 4""")
"""
expected
GABRIEL
RICHARD
RICHARD
GABRIEL
GABRIEL
RICHARD
RICHARD
RICHARD
RICHARD
"""


WIN = "GABRIEL" # can place
LOSE = "RICHARD" # cannot place

def process(data):
	n, x, y = data
	area = x*y
	# choose a valid block but larger than the grid
	for width in range(1, n+1):
		height = math.ceil(n/width)
		filled = n % width == 0
		# print width, height, x, y
		if width > x:
			width, height = height, width
		 	# flip it
		 	if width > x:
		 		return LOSE
		 	if height > y:
		 		return LOSE
		elif height > y:
			width, height = height, width
			if width > x:
				return LOSE
			if height > y:
				return LOSE

		# oxxx
		# oox?
		if not filled:
			# print width, area
			if width == x and area % (n-1) != 0:
				return LOSE
			if height == y and area % (n-1) != 0:
				return LOSE
				
			

	# 2: compute left space
	if area % n > 0:
		return LOSE


	# print "=="

	return WIN

r = TaskRunner(process, DummyRunner)

while neof():
	r.add(int(x) for x in line().split(" "))

r.run(True)