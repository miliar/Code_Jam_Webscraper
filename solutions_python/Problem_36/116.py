from itertools import *
import re

def makematrix(w, h, item = None):
	return [[item for _ in range(w)] for _ in range(h)]


def solve(input, output):
	def readints():
		return map(int, input.readline().split())
	n, = readints()
	welcome = 'welcome to code jam'
	idxes = list(reversed(range(len(welcome))))
	for casen in range(n):
		s = input.readline().strip()
		counts = [1] + [0] * len(welcome)
		for c in s:
			for i in idxes:
				if welcome[i] == c:
					counts[i + 1] = (counts[i] + counts[i + 1]) % 10000
		output.write('Case #%d: %04d\n' % (casen + 1, counts[len(welcome)]))
	output.close()


task = 'C'

#solve(open('%s-small.in' % task, 'r'), open('%s-small.out' % task, 'w'))
solve(open('%s-large.in' % task, 'r'), open('%s-large.out' % task, 'w'))

print 'Yay!' 
