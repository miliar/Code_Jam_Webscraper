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

def solve(D, N, K, S):
	max_time = 0.0
	for i in xrange(N):
		time = float(D - K[i]) / S[i]
		max_time = max(time, max_time)
	return float(D) / max_time

results = []
with open(input_file_name, 'r') as f:
	T = int(f.readline())
	for i in xrange(T):
		line = f.readline().strip('\n')
		D, N = [int(x) for x in line.split(' ')]
		K = []
		S = []
		for j in xrange(N):
			line = f.readline().strip('\n')
			tmp = [int(x) for x in line.split(' ')]
			K.append(tmp[0])
			S.append(tmp[1])
		ret = solve(D, N, K, S)
		results.append(str(ret))

with open(output_file_name, 'w') as f:
	for i in range(len(results)):
		output_string = "Case #%d: %s\n" % (i + 1, results[i])
		print output_string[:-1]
		f.write(output_string)
