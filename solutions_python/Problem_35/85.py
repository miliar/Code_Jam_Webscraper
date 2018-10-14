#! /usr/bin/python

import sys

class Basin(object):
	def __init__(self,grid,w,h):
		self.grid = grid
		self.w, self.h = w,h
		self.deltas = [(0,-1),(-1,0),(1,0),(0,1)] # N W E S
		self.out = [[None for x in xrange(w)] for y in xrange(h)]
		self.next_basin = ord('a')
	def at(self, (x,y)): return self.grid[y][x]
	def delta(self, a,b): return self.at(a) - self.at(b)
	def valid(self, (x,y)): 
		return x >= 0 and y >= 0 and x < self.w and y < self.h
	def neighbours(self, (x,y)):
		return filter(self.valid,[(x+xx,y+yy) for xx,yy in self.deltas])
	def next_available(self):
		b = chr(self.next_basin)
		self.next_basin += 1
		return b
	def get_next_sink(self, (x,y)):
		down = None
		bestd = 0
		for n in self.neighbours((x,y)):
			d = self.delta((x,y),n)
			if d > bestd:
				down,bestd = n,d
		return down
	def get_basin(self, (x,y)):
		if self.out[y][x] != None: return self.out[y][x]
		drain = self.get_next_sink((x,y))
		if drain == None:
			basin = self.next_available()
		else:
			basin = self.get_basin(drain)
		self.out[y][x] = basin
		return basin

if __name__ == "__main__":
	n_tests = int(sys.stdin.readline().strip())

	for testcase in xrange(1,n_tests+1):
		h,w = map(int, sys.stdin.readline().strip().split())
		maplines = [sys.stdin.readline().strip() for i in xrange(h)]
		maplines = [map(int,l.split())  for l in maplines]
		b = Basin(maplines, w=w,h=h)

		print "Case #%d:" % (testcase,)
		for y in xrange(h):
			for x in xrange(w):
				print b.get_basin( (x,y) ),
			print
