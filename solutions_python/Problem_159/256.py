#! /usr/bin/env python

T = int(raw_input())
for t in xrange(T):
	raw = raw_input()
	N = raw.split()
	M = map(int, raw_input().split())
	method1 = 0
	method2 = 0
	prev = M[0]
	for m in xrange(1, len(M)):
		if prev > M[m]:
			method1 = method1 + prev - M[m]
		prev = M[m]
	prev = M[0]
	rate = 0
	for m in xrange(1, len(M)):
		if prev > M[m]:
			x = prev - M[m]
		else:
			x = 0
		if x > rate:
			rate  = x
		prev = M[m]
	# print rate
	for m in xrange(0, len(M)-1):
		if M[m] < rate:
			method2 = method2 + M[m]
		else:
			method2 = method2 + rate
	# method2 = sum(M[:-1]) - M[-1]
	print "Case #%d:" % (t+1), method1, method2
