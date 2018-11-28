#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys

magic="welcome to code jam"
mod=10000

def noccur(s):
	'''Find the number of occurrences of magic as a subsequence of s'''
	dp=(len(magic)+1)*[0]
	dp[0]=1
	for c in s:
		for i in range(1, 1+len(magic)):
			if c==magic[i-1]:
				dp[i]+=dp[i-1]
				dp[i]%=mod
	return dp[len(magic)]

print("\n".join(["Case #{0}: {1:0>4}".format(i+1,noccur(s.strip())) for (i,s) in enumerate(sys.stdin.readlines()[1:]) if not s.isspace() ]))

