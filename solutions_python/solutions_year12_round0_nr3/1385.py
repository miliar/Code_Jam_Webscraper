import re
import math

def p1():
	inputLang = 'ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv '
	outpuLang = 'ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup '
	language = dict()
	language['\n']  = ''
	language['z']  = 'q'
	language['q']  = 'z'

	for i, x in enumerate(inputLang):
		language[x] = outpuLang[i]

	lines = open('A-small-attempt2.in', 'r').readlines()[1:]
	for i, line in enumerate(lines):
		print 'Case #' + str(i+1) + ': ' + ''.join(map(lambda x: language[x], line))

numbers = set()

def generateRecicled(index, max):
	counter = 0
	n = str(index)
	for i in range(len(n)):
		num = int(n[i:] + n[:i])
		pair  = str(index) + '-' + str(num)
		if num <= max and num > index and pair not in numbers: 
			numbers.add(pair)
			counter += 1
	return counter

def solve(start, end):
	count = 0
	for i in xrange(start, end):
		count += generateRecicled(i, end)
	return count
# C-small-attempt0.

lines = open('C-large.in', 'r').readlines()[1:]
for i, line in enumerate(lines):
	numbers = set()
	print 'Case #' + str(i+1) + ': ' + str(solve(int(line.split()[0]), int(line.split()[1])))




