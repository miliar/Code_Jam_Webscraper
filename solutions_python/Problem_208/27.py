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

def solve_single_small(N, E, S, G):
	r = [[(0.0, E[0], S[0])]]
	for i in xrange(1, N):
		tmp = []
		for s in r[i - 1]:
			time = s[0]
			he = s[1]
			hs = s[2]
			if G[i - 1][i] <= he:
				to_i = (time + G[i - 1][i] / float(hs), he - G[i - 1][i], hs)
				tmp.append(to_i)
		min_time = 999999999999999
		for s in tmp:
			min_time = min(s[0], min_time)
		self_i = (min_time, E[i], S[i])
		tmp.append(self_i)
		r.append(tmp)
	min_time = 999999999999999
	for s in r[-1]:
		min_time = min(s[0], min_time)
	return min_time

def floyed(N, Q, E, S, G):
	F = [list(G[i]) for i in xrange(N)]
	for k in xrange(N):
		for i in xrange(N):
			for j in xrange(N):
				if F[i][k] != -1 and F[k][j] != - 1 and (F[i][j] == -1 or F[i][k] + F[k][j] < F[i][j]):
					F[i][j] = F[i][k] + F[k][j]
	for i in xrange(N):
		for j in xrange(N):
			if F[i][j] != -1:
				if F[i][j] > E[i]:
					F[i][j] = -1
				else:
					F[i][j] = F[i][j] / float(S[i])
	for k in xrange(N):
		for i in xrange(N):
			for j in xrange(N):
				if F[i][k] != -1 and F[k][j] != -1 and (F[i][j] == -1 or F[i][k] + F[k][j] < F[i][j]):
					F[i][j] = F[i][k] + F[k][j]
	return F

def solve(N, Q, E, S, G, U, V):
	F = floyed(N, Q, E, S, G)
	ret = ''
	for i in xrange(Q):
		ret += str(F[U[i] - 1][V[i] - 1]) + ' '
	return ret[:-1]

results = []
with open(input_file_name, 'r') as f:
	T = int(f.readline())
	for i in xrange(T):
		line = f.readline().strip('\n')
		N, Q = [int(x) for x in line.split(' ')]
		E = []
		S = []
		for j in xrange(N):
			line = f.readline().strip('\n')
			e, s = [int(x) for x in line.split(' ')]
			E.append(e)
			S.append(s)
		G = []
		for j in xrange(N):
			line = f.readline().strip('\n')
			G.append([int(x) for x in line.split(' ')])
		U = []
		V = []
		for j in xrange(Q):
			line = f.readline().strip('\n')
			u, v = [int(x) for x in line.split(' ')]
			U.append(u)
			V.append(v)
		ret = solve(N, Q, E, S, G, U, V)
		results.append(ret)

with open(output_file_name, 'w') as f:
	for i in range(len(results)):
		output_string = "Case #%d: %s\n" % (i + 1, results[i])
		print output_string[:-1]
		f.write(output_string)
