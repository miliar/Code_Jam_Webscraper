# coding: utf8

import os, sys, re, string

class Robot:
	def __init__(self, stack):
		self.stack = stack
		self.pos = 1
		self.index = 0
		self.size = len(stack)
		self.time = 0

	def is_end(self):
		return self.index >= self.size
	
	def target(self, v):
		return self.index < self.size and self.stack[self.index][0] == v
	
	def move(self):
		dif = abs(self.stack[self.index][1] - self.pos)
		self.pos = self.stack[self.index][1]
		self.time += dif + 1
		self.index += 1
		return dif + 1
	
	def other_move(self, t):
		if self.index >= self.size:
			return
		v = self.stack[self.index][1]
		dif = abs(v - self.pos)
		if dif <= t:
			self.time += t
			self.pos = v
		else:
			self.pos = v + (dif - t)
			self.time += t
		

def solve(line):
	s = line.split(' ')
	N = int(s[0])
	oStack, bStack = [], []
	for i in xrange(N):
		who, button = s[i*2 + 1], s[i*2 + 2]
		if who == 'O':
			oStack.append([i, int(button)])
		else:
			bStack.append([i, int(button)])
	blue, orange = Robot(bStack), Robot(oStack)
	blue.name = 'blue'
	orange.name = 'orange'
	total = 0
	while not blue.is_end() or not orange.is_end():
		if blue.target(total):
			master, slave = blue, orange
		else:
			master, slave = orange, blue
		time = master.move()
		slave.other_move(time)
		total += 1
	return max(blue.time, orange.time)

def main():
	T = int(sys.stdin.readline())
	for i in xrange(T):
		result = solve(sys.stdin.readline().strip())
		print 'Case #%d: %d' % (i + 1, result)

if __name__ == '__main__':
	main()


