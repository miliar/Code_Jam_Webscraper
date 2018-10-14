#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys

if __name__ == "__main__":
	T = int(raw_input())
	for t in xrange(1,T+1):
		R, C = map(int, raw_input().split())
		nq = 0
		chars = []
		grid = [[None for i in xrange(C)] for j in xrange(R)]
		for r in xrange(R):
			line = raw_input()
			for i,c in enumerate(line):
				if c == "?": nq += 1
				else: chars.append((r,i,c))
				grid[r][i] = c
		chars.sort()

		mr = min(map(lambda (r,i,c): r, chars))
		for char in chars:
			cr, cc, x = char
			for i in xrange(cc-1,-1,-1):
				if grid[cr][i] == "?":
					grid[cr][i] = x
					nq -= 1
				else: break
			for i in xrange(cc+1,C):
				if grid[cr][i] == "?":
					grid[cr][i] = x
					nq -= 1
				else: break

		if nq > 0:
			for r in xrange(mr):
				for c in xrange(C):
					grid[r][c] = grid[mr][c]
					nq -= 1
			last_r = mr
			for r in xrange(mr+1,R):
				if grid[r][0] == "?":
					for c in xrange(C):
						grid[r][c] = grid[last_r][c]
						nq -= 1
				else: last_r = r

		print "Case #%d:"%t
		for r in xrange(R):
			print "".join(grid[r])
