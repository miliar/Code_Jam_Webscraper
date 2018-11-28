#!/usr/bin/python3

import sys

def proc(b):
	r = 0
	c = 0
	for i,v in enumerate(b):
		if not v:
			continue
		if c < i:
			r = i - c
			c = i
		c += v
	return r

def proc1(a, b):
	dp = [0 for i in range(a+1)]
	dp[0] = b[0]
	for i in range(1, a+1):
		dp[i] = dp[i-1]
		if dp[i] < i:
			dp[i] = i
		dp[i] += b[i]
	return dp[-1] - sum(b)

t = int(input())

for i in range(1, t+1):
	a,b = input().split(" ")
	a = int(a)
	b = [int(c) for c in b]
	r = proc1(a, b)
	print("Case #%d: %r" % (i, r))