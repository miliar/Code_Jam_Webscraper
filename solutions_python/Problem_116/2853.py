#!/usr/bin/env python

import sys

def loadBoard( input ):
	lines = []
	for i in range( 0, 4 ):
		lines.append( input.readline().strip() )
	input.readline()
	return lines

def getState( lines ):
	winx1 = set()
	winx1.add( 'X' )
	winx1.add( 'T' )
	winx2 = set()
	winx2.add( 'X' )
	wino1 = set()
	wino1.add( 'O' )
	wino1.add( 'T' )
	wino2 = set()
	wino2.add( 'O' )
	vlines = [ '', '', '', '' ]
	dlines = [ '', '' ]
	notCompleted = False
	for l in lines:
		s = set( l )
		if s == winx1 or s == winx2:
			return 'X won'
		if s in wino1 or s == wino2:
			return 'O won'
		if '.' in s:
			notCompleted = True
		for i in range( 0, 4 ):
			vlines[i] = vlines[i] + l[i]
	for l in vlines:
		s = set( l )
		if s == winx1 or s == winx2:
			return 'X won'
		if s == wino1 or s == wino2:
			return 'O won'
		if '.' in s:
			notCompleted = True
	for i in range( 0, 4 ):
		dlines[0] = dlines[0] + lines[i][i]
		dlines[1] = dlines[1] + lines[i][3 - i]
	for l in dlines:
		s = set( l )
		if s == winx1 or s == winx2:
			return 'X won'
		if s == wino1 or s == wino2:
			return 'O won'
		if '.' in s:
			notCompleted = True
	if notCompleted:
		return 'Game has not completed'
	else:
		return 'Draw'

if __name__ == '__main__':
	t = int( sys.stdin.readline() )
	for i in range( 1, t + 1 ):
		sys.stderr.write( 'Test %d\n' % ( i, ) )
		lines = loadBoard( sys.stdin )
		print( 'Case #%d: %s' % ( i, getState( lines ) ) )