#!/usr/bin/env python

import sys

class Motes:
	T = 0
	content = None

	def start(self):
		if len(sys.argv) > 1:
			input = sys.argv[1]
		else:
			input = "input.txt"

		try:
			with open(input) as f:
				self.content = [[int(c) for c in line.split()] for line in f.readlines()]
		except:
			print("Can not find input file: %s" % input)
			sys.exit()

		T = int(self.content[0][0])
		case = 1
		line = 1
		while case <= T:
			self.runCase(case, line)
			case += 1
			line += 2

	def debug(self, str=""):
		print(str)
		pass

	def runCase(self, case, line):
		A,N = self.content[line]
		motes = sorted(self.content[line+1])
		
		if A == 1:
			result = len(motes)
		else:
			result = self.branch(A, motes, 0)

		print("Case #%d: %s" % (case, result))

	def branch(self, A, motes, result):
		if len(motes) == 0: return result
		if A > motes[0]:
			return self.branch(A+motes[0], motes[1:], result)

		return min(
				self.branch(2*A-1, motes, result+1),
				self.branch(A, motes[1:], result+1))

Motes().start()
