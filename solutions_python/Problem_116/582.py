#!/usr/bin/python
'''
2013 qualification round
Problem A. Tic-Tac-Toe-Tomek
'''
import sys
from pprint import pprint
#debug = '-d' in sys.argv
#fh = sys.stdin

fh = open(sys.argv[1])
cases = int(fh.readline())

winkeys = [
	[0, 1],
	[4, 1],
	[8, 1],
	[12, 1],
	[0, 4],
	[1, 4],
	[2, 4],
	[3, 4],
	[0, 5], # diagonal
	[3, 3], # diagonal
	]
wins = []
for start, inc in winkeys:
	wins.append([start + i * inc for i in range(4) ])
#pprint(wins)

def checkboard(b):
	for w in wins:
		me = b[w[0]]
		if me == '.':
			continue
		if me == 'T':
			me = b[w[1]]
			assert me != 'T'
			if me == '.':
				continue
		assert me == 'X' or me == 'O'
		for i in w:
			if b[i] == '.':
				me = 'no'
				break
			if b[i] == 'T':
				continue
			if b[i] != me:
				me = 'no'
				break
		if me == 'X' or me == 'O':
			return me+' won'
	# return None - no winner

for case in range(1, cases+1):
	print 'Case #%i:' % case,
	b = ''.join([ fh.readline().rstrip('\n\r') for i in range(4) ])
	assert fh.readline().strip() == ''
	assert len(b) == 4 * 4
	#print 'checking:', b
	state = checkboard(b)
	if state:
		print state
	elif '.' in b:
		print 'Game has not completed'
	else:
		print 'Draw'
	sys.stdout.flush()
