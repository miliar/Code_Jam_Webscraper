#! /usr/bin/python
import sys
import math

def solve(A, B):
	first = int(math.sqrt(A))

	if first * first < A:
		first += 1

	last = int(math.sqrt(B))
	if last * last > B:
		last -= 1

	ps = 0

	firstPalin = palidromo(first)



	while firstPalin < first:
		firstPalin = nextPalindromo(firstPalin)


	while firstPalin <= last:
		if ehPalindromo(firstPalin * firstPalin):
			#io.write(str(firstPalin) + '\t' + str(firstPalin*firstPalin) + '\n')
			ps += 1

		firstPalin = nextPalindromo(firstPalin)

	return ps

def solve2(A, B):
	
	first = int(math.sqrt(A))

	if first * first < A:
		first += 1

	last = int(math.sqrt(B))
	if last * last > B:
		last -= 1

	ps = 0

	for j in range(first, last + 1):
		if ehPalindromo(j) and ehPalindromo(j * j):
			#io.write(str(j) + '\t' + str(j*j) + '\n')
			ps += 1

	
	return ps

def ehPalindromo(n):
	n  = str(n)
	
	for i in range(len(n)):
		if n[i] != n[len(n) - 1 - i]:
			return False
	
	return True


def palidromo(n):
	n = str(n)
	tam = len(n)
	metadeS = n[:(tam + 1)/2]

	if tam % 2 == 0:
		return int(metadeS + metadeS[::-1])
	else:
		return int(metadeS + metadeS[:-1][::-1])


def nextPalindromo(n):
	n = str(n)
	tam = len(n)
	aux = n[:(tam + 1)/2]
	metade = int(aux)
	aux = len(aux)

	metade += 1
	metadeS = str(metade)

	if len(metadeS) == aux:
		if tam % 2 == 0:
			return int(metadeS + metadeS[::-1])
		else:
			return int(metadeS + metadeS[:-1][::-1])

	else:
		l = tam + 1
		return int('1' + ((l-2)*'0') + '1')


class IOHelper:

	LIST_FILES = ['-small.in', '-large.in', '-test.in' ]

	def __init__(self, letter, filenum):
		self.letter = letter
		self.inputfile = open(str(letter) + IOHelper.LIST_FILES[filenum], 'r')
		self.outputfile = open(str(letter)+"sol-small.out", 'w')
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

io = IOHelper('C', filenum)


for i in range(io.readCases()):
	A, B = io.readInt()
	s = solve(A, B)
	print s
	io.writesol(s)

