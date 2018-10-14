#!/usr/bin/python3

import sys
import heapq
import operator

def solve(w, h, rs):
	ret = []
	done = 0

	corners = []

	x = 0
	while x <= w:
		if done >= len(rs): return ret
		r = rs[done]
		done += 1

		if x > 0: x += r
		if x > w:
			done -= 1
			break
		ret.append((x, 0))

		if (len(corners) < 1) or (r < corners[len(corners)-1][1]):
			corners.append((x+r, r))

		x += r

	while done < len(rs):
		prev_corners = corners
		pcpos = 0
		corners = []
		x = 0
		while x <= w:
			if done >= len(rs): return ret
			r = rs[done]
			done += 1

			while (pcpos+1 < len(prev_corners)) and (x >= prev_corners[pcpos][0]):
				pcpos += 1
			if x > 0: x += r
			if x > w:
				done -= 1
				break

			while (pcpos+1 < len(prev_corners)) and (prev_corners[pcpos][1]+r > h):
				x = prev_corners[pcpos][0]+r
				pcpos += 1
			if x > w:
				done -= 1
				break

			y = prev_corners[pcpos][1]+r
			ret.append((x, y))

			if (len(corners) < 1) or (y+r < corners[len(corners)-1][1]):
				corners.append((x+r, y+r))
			
			x += r


	return ret

def docase():
	line = sys.stdin.readline().split()
	n, w, h = int(line[0]), int(line[1]), int(line[2])
	r = [int(x) for x in sys.stdin.readline().split()]
	order = sorted(range(n), key=(lambda i: -r[i]))
	reverse = [0]*n
	for i in range(n): reverse[order[i]] = i;
	ret = solve(w, h, [r[order[i]] for i in range(n)])
	return " ".join(["%d %d"%ret[reverse[i]] for i in range(n)])

ncases = int(sys.stdin.readline())
case = 0
for case in range(ncases):
       sys.stdout.write("Case #%d: %s\n" % (case+1, docase()))
