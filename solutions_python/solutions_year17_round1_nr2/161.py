#!/usr/bin/python

import sys
import math

if len(sys.argv) != 2:
	print "usage: %s <input_file_name>" % sys.argv[0]
	exit()

input_file_name = sys.argv[1]
if input_file_name[-3:] == ".in":
	output_file_name = input_file_name[:-3] + ".out"
else:
	output_file_name = input_file_name + ".out"

def try_serve(serving, N, P, R, Q, flags):
	chosen = [0] * N
	for i in xrange(N):
		tmp = -1
		lowest_cost = 0
		for j in xrange(P):
			if not flags[i][j]:
				continue
			if R[i] * 0.9 * serving <= Q[i][j] <= R[i] * 1.1 * serving:
				if tmp == -1 or Q[i][j] < lowest_cost:
					tmp = j
					lowest_cost = Q[i][j]
		if tmp == -1:
			return False
		chosen[i] = tmp
	for i in xrange(N):
		flags[i][chosen[i]] = False
	return True

def solve(N, P, R, Q):
	max_serving = 0
	for i in xrange(N):
		for j in xrange(P):
			max_serving = max(max_serving, int(math.floor(Q[i][j] / (R[i] * 0.9))))
	ret = 0
	flags = [[True] * P for i in xrange(N)]
	for serving in xrange(1, max_serving + 1):
		while try_serve(serving, N, P, R, Q, flags):
			ret += 1
	return ret

results = []
with open(input_file_name, 'r') as f:
	T = int(f.readline())
	for i in xrange(T):
		line = f.readline().strip('\n')
		N, P = [int(x) for x in line.split(' ')]
		line = f.readline().strip('\n')
		R = [int(x) for x in line.split(' ')]
		Q = []
		for j in xrange(N):
			line = f.readline().strip('\n')
			Q.append([int(x) for x in line.split(' ')])
		ret = solve(N, P, R, Q)
		results.append(str(ret))

with open(output_file_name, 'w') as f:
	for i in range(len(results)):
		output_string = "Case #%d: %s\n" % (i + 1, results[i])
		print output_string[:-1]
		f.write(output_string)
