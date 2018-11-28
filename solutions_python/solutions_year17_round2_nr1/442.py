#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys

if __name__ == "__main__":
	T = int(raw_input())
	for t in xrange(1,T+1):
		D, N = map(int, raw_input().split())
		ks, ss = [], []
		for i in xrange(N):
			ki, si = map(int, raw_input().split())
			ks.append(ki)
			ss.append(si)
		m = max([(D-ks[i])/float(ss[i]) for i in xrange(N)])
		print "Case #%d: %.6f"%(t,D/float(m))
