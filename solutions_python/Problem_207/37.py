#!/usr/bin/python

import sys
import collections
import math

if len(sys.argv) != 2:
	print "usage: %s <input_file_name>" % sys.argv[0]
	exit()

input_file_name = sys.argv[1]
if input_file_name[-3:] == ".in":
	output_file_name = input_file_name[:-3] + ".out"
else:
	output_file_name = input_file_name + ".out"

def solve_small(N, R, Y, B):
	d = {'R': R, 'Y': Y, 'B': B}
	maximum = 0
	max_color = ''
	for key in d:
		if d[key] > maximum:
			maximum = d[key]
			max_color = key
	ret = max_color
	d[max_color] -= 1
	for i in xrange(N - 1):
		maximum = 0
		max_color = ''
		last_color = ret[-1]
		for key in d:
			if key != last_color and (d[key] > maximum or (d[key] == maximum and key == ret[0])):
				maximum = d[key]
				max_color = key
		if max_color == '':
			return 'IMPOSSIBLE'
		ret += max_color
		d[max_color] -= 1
	if ret[0] == ret[-1]:
		return 'IMPOSSIBLE'
	return ret

def solve(N, R, O, Y, G, B, V):
	'''
		O <-> B
		G <-> R
		V <-> Y
	'''
	if R == Y == G == V == 0:
		if B != O:
			return 'IMPOSSIBLE'
		else:
			return 'BO' * (N / 2)
	elif O == Y == B == V == 0:
		if G != R:
			return 'IMPOSSIBLE'
		else:
			return 'GR' * (N / 2)
	elif R == O == G == B == 0:
		if V != Y:
			return 'IMPOSSIBLE'
		else:
			return 'VY' * (N / 2)
	if not ((O == 0 or B > O > 0) and (G == 0 or R > G > 0) and (V == 0 or Y > V > 0)):
		return 'IMPOSSIBLE'
	simple_ret = solve_small(N - (O + G + V) * 2, R - G, Y - V, B - O)
	if simple_ret == 'IMPOSSIBLE':
		return simple_ret
	if O > 0:
		idx = simple_ret.index('B')
		simple_ret = simple_ret[:idx] + 'BO' * O + simple_ret[idx:]
	if G > 0:
		idx = simple_ret.index('R')
		simple_ret = simple_ret[:idx] + 'RG' * G + simple_ret[idx:]
	if V > 0:
		idx = simple_ret.index('Y')
		simple_ret = simple_ret[:idx] + 'YV' * V + simple_ret[idx:]
	return simple_ret

results = []
with open(input_file_name, 'r') as f:
	T = int(f.readline())
	for i in xrange(T):
		line = f.readline().strip('\n')
		N, R, O, Y, G, B, V = [int(x) for x in line.split(' ')]
		ret = solve(N, R, O, Y, G, B, V)
		results.append(ret)

with open(output_file_name, 'w') as f:
	for i in range(len(results)):
		output_string = "Case #%d: %s\n" % (i + 1, results[i])
		print output_string[:-1]
		f.write(output_string)
