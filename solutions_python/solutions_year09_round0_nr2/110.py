from itertools import *
import re

def makematrix(w, h, default = None):
	return [[None for _ in range(w)] for _ in range(h)]


def solve(input, output):
	def readints():
		return map(int, input.readline().split())
	t, = readints()
	for casen in range(t):
		h, w = readints()
		border = [9999999]
		lborder = [border * (w + 2)]
		hmap = (lborder + 
			[border + readints() + border for _ in range(h)]
			+ lborder)
		lmap = makematrix(w + 2, h + 2)
		
		def process(row, col, currletter):
			stack = []
			while True:
				letter = lmap[row][col]
				if letter: break
				stack.append((row, col))
				h = hmap[row][col]
				dirs = (
					(row - 1, col    ), 
					(row    , col - 1), 
					(row    , col + 1), 
					(row + 1, col    ))
				mh, d = min((hmap[d[0]][d[1]], d) for d in dirs)  

				if mh < h:
					row, col = d
				else:
					letter = currletter
					currletter = chr(ord(currletter) + 1)
					break;

					
			for row, col in stack:
				lmap[row][col] = letter
			return currletter
		
		currletter = 'a'
		for row in range(1, h + 1):
			for col in range(1, w + 1):
				currletter = process(row, col, currletter)
	
		output.write('Case #%d:\n' % (casen + 1))
		for row in lmap[1:-1]:
			output.write(' '.join(row[1:-1]))
			output.write('\n')
	output.close()


task = 'B'

#solve(open('%s-small.in' % task, 'r'), open('%s-small.out' % task, 'w'))
solve(open('%s-large.in' % task, 'r'), open('%s-large.out' % task, 'w'))

print 'Yay!' 
