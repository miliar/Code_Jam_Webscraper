#!/usr/bin/python

import sys

DBG = False

pouet = 0

def solve(matrix):
	global pouet
	x, o, diagx, diago = 0, 0, 0, 0
	t, diagt = False, False
	draw = True
	for k in xrange(0, 4): # row
		t = False
		x, o = 0,0
		for l in xrange(0, 4): # col
			c = matrix[k][l]
			if c == '.':
				draw = False
			if c == T:
				t = True
				if x >= 3:
					if DBG:
						pouet += 1
						print "Pouet1", pouet
					p('X won')
					return
				elif o >= 3:
					p('O won')
					return
			if c == X:
				x += 1
				if x >= 4 or (x >= 3 and t is True):
					if DBG:
						pouet += 1
						print "Pouet2", pouet
						print "HAHA"
					p('X won')
					return
			elif c == O:
				o += 1
				if o >= 4 or (o >= 3 and t is True):
					p('O won')
					return
			if k == l:
				if c == T:
					diagt = True
				if diagx >= 3:
					if DBG:
						pouet += 1
						print "Pouet3", pouet
					p('X won')
					return
				elif diago >= 3:
					p('O won')
					return
				if c == X:
					diagx += 1
					if diagx >= 4 or (diagx >= 3 and diagt is True):
						if DBG:
							pouet += 1
							print "Pouet4", pouet
						p('X won')
						return
				elif c == O:
					diago += 1
					if diago >= 4 or (diago >= 3 and diagt is True):
						p('O won')
						return
	x, o, diagx, diago = 0, 0, 0, 0
	t, diagt = False, False
	for k in xrange(3, -1, -1): # col
		x, o = 0, 0
		t = False
		for l in xrange(3, -1, -1): # row
			c = matrix[l][k]
			if c == '.':
				draw = False
			if c == T:
				t = True
				if x >= 3:
					if DBG:
						pouet += 1
						print "Pouet5", pouet
					p('X won')
					return
				elif o >= 3:
					p('O won')
					return
			if c == X:
				x += 1
				if x >= 4 or (x >= 3 and t is True):
					if DBG:
						pouet += 1
						print "Pouet6", pouet
					p('X won')
					return
			elif c == O:
				o += 1
				if o >= 4 or (o >= 3 and t is True):
					p('O won')
					return
			if (3-k) == l:
				if DBG:
					print "Diag: ", (k, l, 3-k)
				if c == T:
					diagt = True
					if diagx >= 3:
						if DBG:
							pouet += 1
							print "Pouet7", pouet
						p('X won')
						return
					elif diago >= 3:
						p('O won')
						return
				if c == X:
					diagx += 1
					if diagx >= 4 or (diagx >= 3 and diagt is True):
						if DBG:
							pouet += 1
							print "Pouet8", pouet
						p('X won')
						return
				elif c == O:
					diago += 1
					if diago >= 4 or (diago >= 3 and diagt is True):
						p('O won')
						return
	if draw is True:
		p("Draw")
	else:
		p("Game has not completed")

def p(s):
	sys.stdout.write(s)

n = int(raw_input())

X, O, T = 'X', 'O', 'T'

for j in xrange(1, n+1):

	p("Case #" + str(j) + ": ")
	i = 4
	matrix = []
	for x in xrange(0, 4):
		matrix.append([c for c in raw_input().strip()])
		i -= 1
	if DBG:
		print matrix
		pouet = 0
	solve(matrix)
	p("\n")
	try:
		raw_input() # blank line at the end of the test case
	except EOFError:
		pass