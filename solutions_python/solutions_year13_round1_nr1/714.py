#! /usr/bin/python
import sys
import math
def solve(r, t):

	a = float(2)
	b = float(2*r -1)
	c = float(-t )

	delta = b*b - 4 * a * c


	sol = (-b + math.sqrt(delta))/ (2 * a)

	sol = int(sol)

	while f(a,b,c,sol) > 0:
		sol -= 1

	if sol < 0:
		sol = 0

	return sol


def f(a,b,c,x):
	return a*x*x + b*x + c








class IOHelper:

	LIST_FILES = ['-small.in', '-large.in', '-test.in' ]

	def __init__(self, letter, filenum):
		self.letter = letter
		self.inputfile = open(str(letter) + IOHelper.LIST_FILES[filenum], 'r')
		self.outputfile = open(str(letter)+"sol2.out", 'w')
		self.i = 1

	def readCases(self):
		return int(self.inputfile.readline())

	def readLines(self, n):
		lines = []
		for i in range(n):
			lines.append(self.readline())
		return lines

	def readline(self):
		return self.inputfile.readline()

	def writesol(self, sol):
		s = 'Case #' + str(self.i) + ': ' + str(sol) + '\n'
		print s
		self.i += 1
		self.write(s)

	def write(self, t):
		self.outputfile.write(t)

	def readInt(self):
		return [int(x) for x in self.readline().split(' ')]

	@staticmethod
	def solution(i, sol):
		return "Case #" + str(i + 1) + ": " + str(sol) + '\n'



filenum = 2
if len(sys.argv) > 1:
	filenum = int(sys.argv[1])

io = IOHelper('A', filenum)


for i in range(io.readCases()):
	tab = []

	s = io.readInt()

	r = s[0]
	t = s[1]


	s = solve(r, t)
	io.writesol(s)
