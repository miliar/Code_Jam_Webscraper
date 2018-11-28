#!/usr/bin/python

import math
import sys


def gen_triples (s):
	ret = []

# pretty ugly, actually, with exponential running time...
# lazy saturday night...
# also, back of the envelope calculation...  seems a bit off but 
# includes the valid triples.
	avg = s / 3.0
	x1min = int (math.floor (avg - 4/3))
	if x1min < 0: x1min = 0

	x1max = int (math.ceil (2*avg - 4/3))
	if x1max < 0: x1max = 0

	x3min = int (math.floor (avg + 2/3))
	if x3min < 0: x2min = 0

	x3max = int (math.ceil (2*avg + 2/3))
	if x3max < 0: x3max = 0

#	print "x1min: ", x1min, ", x1max: ", x1max
#	print "x3min: ", x3min, ", x3max: ", x3max

	for x1 in range (x1min, x1max+1):
		for x2 in range (x1min, x3max+1):
			for x3 in range (x3min, x3max+1):
#				print "testing ", x1, x2, x3
				if (s == x1+x2+x3) \
				and (x1 <= x2) and (x2 <= x3) \
				and ((x3 - x1) <= 2):
					ret.append ((x1, x2, x3))

	return ret



def is_surprise (t):
	return (t[2]-t[0]) == 2



def inc_indices (i):
	i[0] += 1

	n = 0
	while n < len (i):
		if i[n] > max_indices[n]:
			i[n] = 0

			if n+1 == len (i):
				return

			i[n+1] += 1
		else:
			break

		n += 1
		


num_testcases = int (sys.stdin.readline())

for n in range(1, num_testcases+1):
	line = sys.stdin.readline().split()
	num_g = int(line[0])
	num_surprises = int(line[1])
	threshold = int(line[2])
	points = map (lambda x: int (x), line[3:])
#	print points

	cand = []
	surprises = []
	for p in points:
		cand.append (gen_triples (p))

#	print "cand: ", cand
	surprises = [map (lambda x: is_surprise (x), p) for p in cand]
	indices = [0 for p in cand]
	indices_start = [0 for p in cand]
	max_indices = [(len (p) - 1) for p in cand]
#	print "surprises: ", surprises
#	print indices
#	print max_indices

	num_above_threshold = 0

	while True:
		act_surprises = len (filter (lambda x: x, \
				[surpr[indices[index]] for index, surpr \
					in enumerate (surprises)]))

#		print "indices: ", indices
#		print "num surprises: ", act_surprises

		if act_surprises == num_surprises:
			possibility = [l[indices[index]] for index, l \
					in enumerate (cand)]

			# x1 <= x2 <= x3 sufficient if largest value >= thresh
			cur_above_threshold = len (filter (lambda x: x, map ( \
				lambda x: x[2] >= threshold, possibility)))

#			print possibility, cur_above_threshold
			if cur_above_threshold > num_above_threshold:
				num_above_threshold = cur_above_threshold

		inc_indices (indices)
		if (indices == indices_start): break

	print "Case #%d: %d" % (n, num_above_threshold)
