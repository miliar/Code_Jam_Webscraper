#!/usr/bin/env python
import math

T = int(raw_input())
for t in xrange(T):
	C,F,X = map(float,raw_input().split())
	n = max(0,int(math.ceil(X/C - 1. - 2./F)))
	ans = X/(2.+n*F)
	for i in xrange(n):
		ans += C/(2.+i*F)
	print 'Case #%d: %.7f' % (t+1,ans)
	

