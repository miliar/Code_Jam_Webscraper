#!/usr/bin/env python

from __future__ import print_function
import math
import sys

with open(sys.argv[1]) as f:
	for case in range(1, int(f.readline().strip()) + 1):
		N, K = map(int, f.readline().strip().split())
		pancakes = []
		for i in range(N):
			radius, height = map(float, f.readline().strip().split())
			walls = 2 * math.pi * radius * height
			top = math.pi * radius * radius
			pancakes += [(walls, top)]
		pancakes.sort(reverse=True)
		selected_by_walls = pancakes[:K]
		selected_by_top = sorted(selected_by_walls, key=lambda x: x[1], reverse=True)
		remaining_by_walls = pancakes[K:]
		remaining_by_top = sorted(remaining_by_walls, key=lambda x: x[1], reverse=True)
		for w, t in remaining_by_walls:
			if t > selected_by_top[0][1] \
			and t - selected_by_top[0][1] - selected_by_walls[-1][0] + w > 0:
				selected_by_walls[-1] = (w, t)
				selected_by_walls.sort(reverse=True)
				selected_by_top = sorted(selected_by_walls, key=lambda x: x[1], reverse=True)
		syrup = reduce(float.__add__, zip(*selected_by_walls)[0]) + selected_by_top[0][1]
		print('Case #%s: %.9f' % (case, syrup))