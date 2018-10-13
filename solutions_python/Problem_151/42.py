#!/usr/bin/python

import sys

def calc(ss):
	if len(ss) == 0: return 0
	t = set(ss)
	for s in ss:
		for i in xrange(len(s)):
			t.add(s[:i])
	return len(t)

TT = int(sys.stdin.readline())

for T in xrange(1,TT+1):
	M, N = map(int, sys.stdin.readline().split())
	S = [ sys.stdin.readline().strip() for _ in xrange(M) ]

	ans1, ans2 = 0, 0
	for smask in xrange(N**M):
		m = smask
		SS = [ [] for _ in xrange(N) ]
		for s in S:
			SS[m%N].append(s)
			m /= N
		nnode = sum( calc(ss) for ss in SS )
		if nnode > ans1:
			ans1, ans2 = nnode, 1
		elif nnode == ans1:
			ans2 += 1

	print "Case #%d: %d %d" % (T, ans1, ans2%1000000007)


