#!/usr/bin/python
#
# Google Code Jam
#
#

import sys
import os

debug=False

def checkwin(board,i,j,idiff,jdiff):
	global k
	for x in xrange(0, k):
		ii = i+(idiff*x)
		jj = j+(jdiff*x)
		if ii < 0 or ii >= len(board): return False
		if jj < 0 or jj >= len(board): return False
		if board[i+(idiff*x)][j+(jdiff*x)] != board[i][j]: return False
	return True

def solve_test_case(board, k, n):
	board2 = []
	while len(board2) < n: board2.append(['.' for _ in xrange(0,n)])
	jj = 0
	ii = len(board) - 1
	for i in xrange(n-1, -1, -1):
		for j in xrange(n-1, -1, -1):
			if debug: 
				print "checking (%d,%d) = %s" % (i,j,board[i][j])
			if board[i][j] == '.': continue
			r = board2[ii]
			r[jj] = board[i][j]
			if debug:
				print "setting (%d,%d) = (%d,%d)" % (ii,jj,i,j)
				print "board2:"
				for row in board2: print row

			ii -= 1
		ii = len(board) - 1
		jj += 1

	if debug:
		print "board:"
		for row in board: print row
		print "board2:"
		for row in board2: print row
		print ""

	r = {'R':False, 'B':False}
	for i in xrange(0, n):
		for j in xrange(0,n):
			v = board2[i][j]
			if v == '.': continue
			if r[v]: continue
			if checkwin(board2,i,j,1,0) or checkwin(board2,i,j,0,1) or checkwin(board2,i,j,1,-1) or checkwin(board2,i,j,1,1):
				r[v] = True

	if r['R'] and r['B']: return "Both"
	if r['R']: return "Red"
	if r['B']: return "Blue"
	return "Neither"
		

if __name__ == '__main__':
    input = open(sys.argv[1])
    if len(sys.argv) > 2 and sys.argv[2] == "--debug": debug=True
    test_case_count = int(input.readline().strip())
    test_case = 0
    while test_case < test_case_count:
	n,k = map(int, input.readline().strip().split())
	board = []
	while len(board) < n:
		board.append(list(input.readline().strip()))
        test_case += 1
        print "Case #%d: %s" % (test_case, solve_test_case(board, k, n))


 
            
 
