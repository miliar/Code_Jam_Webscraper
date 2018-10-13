#!/usr/bin/env python3
import sys, array

def solution(R, C, a):
	for x in range(0, C):
		for y in range(0, R):
			if a[y][x] == '#':
				if x < C - 1 and y < R - 1:
					for (xx,yy) in [ (x, y), (x, y+1), (x+1,y+1), (x+1,y) ]:
						if a[yy][xx] == '#':
							if (x + y) % 2 == (xx + yy) % 2:
								a[yy][xx] = '/'
							else:
								a[yy][xx] = '\\'
						else:
							return "Impossible"
				else:
					return "Impossible"
	return "\n".join([ ''.join(row) for row in a ])

f = iter("""3
2 3
###
###
1 1
.
4 5
.##..
.####
.####
.##..""".splitlines());

f = open("/home/martin/Downloads/A-large.in")

cases = int(next(f))

for case in range(1, cases + 1):
	(R, C) = (int(s) for s in next(f).split())
	a = [ list(next(f).strip()) for i in range(1, R + 1) ]
	
	print("Case #%d:" % case)
	print(solution(R, C, a))
