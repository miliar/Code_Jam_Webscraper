#!/usr/bin/env python

from math import pi
from operator import itemgetter
import itertools
from multiset import *

def get_area(pancakes):
	circle = pancakes[0][0] ** 2 * pi
	area = circle + 2 * pi * pancakes[0][0] * pancakes[0][1]

	for i in xrange(1, len(pancakes)):
		area += pancakes[i][0] ** 2 * pi + 2 * pi * pancakes[i][0] * pancakes[i][1] - circle
		circle = pancakes[i][0] ** 2 * pi
	return area

def find_max(pancakes, k):
	comb = set(itertools.combinations(pancakes, k))
	max = 0
	for _ in xrange(0, len(comb)):
		pan = sorted(comb.pop(), key=itemgetter(0))
		value = get_area(pan)
		if value > max:
			max = value
	return max


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	n, k = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
	pancakes = Multiset()
	for j in xrange(1, n + 1):
		r, h = [int(s) for s in raw_input().split(" ")]
		pancakes.add((r, h))
	max = find_max(pancakes, k)
	print "Case #{}: {}".format(i, max)