#!/usr/bin/env python

GRID_SIZE = 4

def check_line(line):
	counter = {}
	for i in xrange(len(line)):
		if line[i] in counter:
			counter[line[i]] += 1
		else:
			counter[line[i]] = 1
	for letter in counter:
		if letter != '.':
			if counter[letter] == 4:
				return letter
			elif counter[letter] == 3 and 'T' in counter and counter['T'] == 1:
				return letter
	return ''

N = int(raw_input())

for n in xrange(N):
	grid = []
	whole_game = ''
	for j in xrange(GRID_SIZE):
		grid.append(raw_input())
		whole_game += grid[j]
	raw_input()

	winner = ''

	# check horizontals...
	for line in grid:
		winner = check_line(line)
		if (winner != ''):
			break

	# check verticals...
	if winner == '':
		for i in xrange(len(grid[0])):
			line = ''
			for j in xrange(len(grid)):
				line += grid[j][i]
			winner = check_line(line)
			if winner != '':
				break
	
	# check diagonals...
	if winner == '':
		line = ''
		for i in xrange(len(grid)):
			line += grid[i][i]
		winner = check_line(line)
	if winner == '':
		line = ''
		for i in xrange(len(grid)):
			line += grid[3-i][i]
		winner = check_line(line)
	
	# check for a draw and print out the winner...
	if winner == '':
		if '.' in whole_game:
			print 'Case #%d: Game has not completed' % (n+1)
		else:
			print 'Case #%d: Draw' % (n+1)
	else:
		print 'Case #%d:' % (n+1), winner, 'won'
