#!/usr/bin/env python

from collections import deque

global debug,ins,oj,bl

class bot:
	def __init__(self, name):
		self.name = name
		self.pos = 1
		self.ins = deque()

	def act(self, s):
		global debug
		if (debug):
			print "%s.act(%s)" % (self.name, s),

		press = False
		if (len(self.ins) == 0):
			if (debug):
				print "Stay at button", self.pos
			return False

		if ((self.pos == self.ins[0]) and (self.name == s)):
			self.ins.popleft()
			press = True
			if (debug):
				print "Push button", self.pos
		elif (self.pos > self.ins[0]):
			self.pos -= 1
			if (debug):
				print "Move to button", self.pos
		elif (self.pos < self.ins[0]):
			self.pos += 1
			if (debug):
				print "Move to button", self.pos
		else:
			if (debug):
				print "Stay at button", self.pos

		return press


def parse_in():
	global debug, ins, oj, bl

	for i in range(1,len(ins)):
		if (ins[i] == 'O'):
			oj.ins.append(int(ins[i+1]))
		elif (ins[i] == 'B'):
			bl.ins.append(int(ins[i+1]))

	if (debug):
		print "oj instructions =", oj.ins
		print "bl instructions =", bl.ins

def eval():
	global debug, ins, oj, bl
	t = 0
	i = 1
	while (i < len(ins)):
		if (debug):
			print "Time:", (t+1)
		action = False

		if (oj.act(ins[i])):
			action = True
		if (bl.act(ins[i])):
			action = True

		t+=1
		if (action):
			i+=2

	return t

def main():
	global debug, ins, oj, bl
	debug = False
	cases = int(raw_input())

	for n in range(1,cases+1):
		ins = []
		oj = bot('O')
		bl = bot('B')

		ins = raw_input().split() #instructions input
		if (debug):
			print ins

		parse_in()
		t = eval()
		print "Case #%s:" % n, t

	return 0

main()
