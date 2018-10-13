# Author: Brian Armstrong
# Code Jam 2009
# Qualification Round
# Problem B: Watersheds

import sys, os
import string

class MapTile(object):
	# Basins represented by a digraph going in reverse
	# 	This means that the nodes make up a digraph that flows *up*,
	#	not down.
	def __init__(self, alt, y, x):
		self.alt = alt
		self.x = x
		self.y = y
		self.upstream = []
		self.sink = None
		self.label = None
	def append(self, tile):
		self.upstream.append(tile)

class BasinMap(object):
	# Each location in the map is a MapTile

	def __init__(self, h, w):
		self.h = h
		self.w = w
		self.m = [None] * h
		for y in range(0, self.h):
			self.m[y] = [None] * self.w
		self.inserted = 0
		self.sinks = [] # This stores sinks in order
	def insert(self, locs):
		# Insert one row at a time!
		# This is O(h * w)
		n = 0
		for loc in locs:
			tile = MapTile(loc, self.inserted, n)
			self.m[self.inserted][n] = tile
			n += 1
		self.inserted += 1
	def graph(self):
		# This is also O(h * w)
		for y in range(0, self.h):
			for x in range(0, self.w):
				has_N = (y != 0)
				has_S = (y != self.h - 1)
				has_W = (x != 0)
				has_E = (x != self.w - 1)

				here = self.m[y][x]
				lower = None
				lower_alt = here.alt

				# tiebreaker order is N, W, E, S
				if has_N and self.m[y-1][x].alt < lower_alt:
					lower = self.m[y-1][x]
					lower_alt = lower.alt

				if has_W and self.m[y][x-1].alt < lower_alt:
					lower = self.m[y][x-1]
					lower_alt = lower.alt
				
				if has_E and self.m[y][x+1].alt < lower_alt:
					lower = self.m[y][x+1]
					lower_alt = lower.alt

				if has_S and self.m[y+1][x].alt < lower_alt:
					lower = self.m[y+1][x]
					lower_alt = lower.alt

				if lower is None:
					self.sinks.append(here)
				else:
					lower.upstream += [here]


	def labels(self):
		l = [None] * self.h
		for n in range(0, self.h):
			l[n] = [None] * self.w

		labellist = string.lowercase[:]

		sinkd = {}

		for a in self.sinks:
			sinkd[a] = [a]
			a.sink = a
			ups = a.upstream[:]
			while len(ups) != 0:
				up = ups.pop()
				if up.sink is None:
					up.sink = a
					sinkd[a] += [up]
					ups += up.upstream


		for y in range(0, self.h):
			for x in range(0, self.w):
				if self.m[y][x].label is None:
					s = self.m[y][x].sink
					lbl = labellist[0]
					labellist = labellist[1:]
					for t in sinkd[s]:
						t.label = lbl
				l[y][x] = self.m[y][x].label

		return l




def print_cases(cases):
	n = 1
	for case in cases:
		print "Case #" + str(n) + ":"
		for line in case:
			print ' '.join(line)
		n = n + 1

def main():
	input_t = int(sys.stdin.readline().rstrip())
	cases = []
	for t in range(0, input_t):
		dims = sys.stdin.readline().split()
		h = int(dims[0])
		w = int(dims[1])

		m = BasinMap(h, w)

		for y in range(0, h):
			row = sys.stdin.readline().split()
			row = map(int, row)
			m.insert(row)

		m.graph()

		cases.append(m.labels())

	print_cases(cases)


if __name__ == "__main__":
	main()

