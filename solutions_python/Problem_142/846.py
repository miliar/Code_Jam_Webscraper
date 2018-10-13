#!/usr/bin/env python

import sys

def uid(string):
	u = [[string[0], 1]]
	for i in range(1,len(string)):
		if string[i] != string[i-1]:
			u.append([string[i], 1])
			continue
		u[-1][1] += 1
	return u

def dist(string1, string2):
	d = 0
	u = uid(string1)
	v = uid(string2)
	if len(u) != len(v): return -1
	for i in range(len(u)):
		if u[i][0] != v[i][0]: return -1
		d += abs(u[i][1] - v[i][1])
	return d
		

f = sys.stdin

T = int(f.readline().strip())

for i in range(1, T+1):
	N = int(f.readline().strip())
	strings = []
	for k in range(N):
		strings.append(f.readline().strip())
	min_dist = 100000000
	possible = 1
	for s1 in strings:
		tot_d = 0
		for s2 in strings:
			d = dist(s1, s2)
			if d == -1:
				possible = 0
				break
			tot_d += d
		if possible == 0: break
		if tot_d < min_dist: min_dist = tot_d
	if possible == 1:
		print "Case #%s: %s" % (i, min_dist)
	else:
		print "Case #%s: Fegla Won" % i
