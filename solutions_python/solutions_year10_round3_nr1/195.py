#!/usr/bin/env python
# -*- coding: utf-8 -*-


def func(n, l):
	l = sorted(l, key=lambda w: w[0])
	l2 = sorted(l, key=lambda w: w[1])
	i = 0
	s=0
	for w in l:
		#j = i
		for w2 in l[i+1:]:
			if (w[0] > w2[0] and w[1] < w2[1]) or (w2[0] > w[0] and w2[1] < w[1]):
				s+=1
		i = i+1
	return s

if __name__ == '__main__':
	N = int(raw_input())
	for i in range(1, N+1):
		n = int(raw_input())
		l = []
		for j in range(1,n+1):
			l.append([int(j) for j in raw_input().split()])
		print "Case #%d: %s" % (i, func(n, l))
