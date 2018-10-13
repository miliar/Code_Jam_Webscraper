#!/usr/bin/python
# -*- coding: utf-8 -*-

def allpartitions(S, N):
	partitions = [[[] for server in range(N)]]
	for s in S:
		newpartitions = []
		for p in partitions:
			for server in range(N):
				newp = list(p)
				newserver = list(p[server])
				newserver.append(s)
				newp[server] = newserver
				newpartitions.append(newp)
		partitions = newpartitions
	return partitions
	
def valid(partition):
	for server in partition:
		if len(server)==0:
			return False
	return True
	
def sizeTrie(S):
	n = 0
	root = dict()
	for s in S:
		cur_dict = root
		for c in s:
			if not c in cur_dict:
				n += 1
			cur_dict = cur_dict.setdefault(c, {})
		cur_dict = cur_dict.setdefault('', '')
	return n + 1

def solve(S, N):
	cur_max = 0
	cur_times = 0
	for partition in allpartitions(S, N):
		if valid(partition):
			s = sum([sizeTrie(server) for server in partition])
			if (s>cur_max):
				cur_times = 0
				cur_max = s
			if (s==cur_max):
				cur_times += 1
	return str(cur_max) + " " + str(cur_times)
			

T = int(input())
for test in range(T):
	[M,N] = [int(i) for i in input().split()]
	S = []
	for s in range(M):
		S.append(input())
	print ('Case #%d:' % (test+1), solve(S, N))
