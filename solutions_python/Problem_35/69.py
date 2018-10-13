#!/usr/bin/python

import heapq


def merge(sets, a, b):
	aRoot = parent(sets,a)
	bRoot = parent(sets,b)
	sets[aRoot] = bRoot

def parent(sets, a):
	if sets[a] == -1:
		return a
	else:
		sets[a] = parent(sets,sets[a])
		return sets[a]

ADJ = ((-1,0),(0,-1),(0,1),(1,0))

T = int(raw_input())

for Case in xrange(1,T+1):
	H,W = tuple(int(i) for i in raw_input().split())
	
	mp = []
	heap = []

	for row in xrange(H):
		mp.append([int(i) for i in raw_input().split()])
		for i,j in enumerate(mp[row]):
			heapq.heappush(heap,(-j,(row,i)))
	
	
	
	sets = [-1] * W * H
	
	seen = {}
	
	while(len(heap) > 0):
		front = heapq.heappop(heap)
		y,x = front[1]
		height = mp[y][x]
		
		
		#print height,front[1],
		
		best = height
		
		for dy,dx in ADJ:
			if ((y+dy) >= 0 and (y+dy) < H and 
				(x+dx) >= 0 and (x+dx) < W):
				if (mp[y+dy][x+dx]) < best:
					best = mp[y+dy][x+dx]
					bestloc = (y+dy,x+dx)
		
		if (best < height):
			#print " -> ",bestloc
			# Flow to bestloc.
			merge(sets, y*W+x, 
				bestloc[0]*W + bestloc[1])
		#else: print
		
			
	curset = 0
	print "Case #%d:" % Case

	for i in xrange(H):
		for j in xrange(W):
			p = parent(sets, i*W + j)
			if p not in seen:
				seen[p] = curset
				curset += 1
			print chr(seen[p] + 97),
			assert(curset <= 26)
		print
	
		