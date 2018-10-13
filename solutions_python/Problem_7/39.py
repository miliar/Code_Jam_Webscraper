#!/usr/bin/env python
import sys, math


cases = int(raw_input())
for num in range(cases):
	n_trees, A, B, C, D, x0, y0, M = map(int, raw_input().split(' '))

	points = []
	X = x0
	Y = y0
	points.append(X + Y*1j)
	for i in range(1, n_trees):
		X = (A * X + B) % M
		Y = (C * Y + D) % M
		points.append(X + Y*1j)
	
	def ok(i, j, k):
		tot = points[i] + points[j] + points[k]
		return (tot.real % 3) == (tot.imag % 3) == 0
	
	n_triangles = 0
	for i in range(0, n_trees):
		for j in range(i + 1, n_trees):
			for k in range(j + 1, n_trees):
				if ok(i, j, k):
					n_triangles += 1

	print "Case #%d: %d" % (num + 1, n_triangles)
