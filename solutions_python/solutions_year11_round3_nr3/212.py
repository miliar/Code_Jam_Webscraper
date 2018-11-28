#!/usr/bin/python
# -*- coding: utf-8 -*-
## Problem C. Perfect Harmony (GCJ Round 1B 2011)


def harmony(tab):
	sol = -1
	
	for k in xrange(L, H+1):
		for h in tab:
			if h % k == 0 or k % h == 0:
				sol = k
			else:
				sol = -1
				#print k, h
				break
		if sol == k:
			break
		#print "k =", k, " : ", ", ".join(str(h % k) for h in tab), " ou ", ", ".join(str(k % h) for h in tab)
	
	if sol == -1:
		return "NO"
	else:
		return str(sol)
	return "oups"


if __name__ == "__main__":
	T = int(raw_input())
	for k in xrange(T):
		N, L, H = map(int, raw_input().split())
		#print N, H, L
		tab = map(int, raw_input().split())
		#print tab
		char = "Case #%d: %s" %(k+1, harmony(tab))
		print char