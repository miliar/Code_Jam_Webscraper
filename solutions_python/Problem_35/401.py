#!/usr/bin/env python

import sys
import re

def findmin(h, w, map, H, W):
	while 1:
		tmp = map[h][w]
		north = 10000
		west = 10000
		east = 10000
		south = 10000
		if (h > 0):
			north = map[h-1][w]
		if (w > 0):
			west = map[h][w-1]
		if (w < W-1):
			east = map[h][w+1]
		if (h < H-1):
			south = map[h+1][w]
		arr = [north, west, east, south]
		minimum = min(arr)
		if (minimum < tmp):
			if minimum == north:
				h = h - 1
				continue
			if minimum == west:
				w = w - 1
				continue
			if minimum == east:
				w = w + 1
				continue
			if minimum == south:
				h = h + 1
				continue
		break
	return (h, w)


T = int(sys.stdin.readline().strip())
for i in range(1, T+1):
	(H, W) = map(int, sys.stdin.readline().split())
	dmap = []
	minh = 0
	minw = 0
	minv = 10000
	for j in range(0, H):
		dmap.append(map(int, sys.stdin.readline().split()))
	
	mapf = dmap
	mins = {}
	fill = 'abcdefghijklmnopqrstuvwxyz'
	for h in range(0, H):
		for w in range(0, W):
			mincell = findmin(h, w, dmap, H, W)
			if mincell not in mins.keys():
				val = fill[len(mins.keys())]
#				for key in mins.keys():
#					if dmap[mincell[0]][mincell[1]] < dmap[key[0]][key[1]]:
#						val = min(val, mins[key])
#						mins[key] = fill[fill.index(mins[key])+1]
				mins[mincell] = val

	print "Case #%s:" % i
	for h in range(0, H):
		line = ''
		for w in range(0, W):
			mincell = findmin(h, w, dmap, H, W)
			line = line + mins[mincell] + ' '
		print line
