#! /usr/bin/python
from sys import stdin
import psyco
psyco.full()

def fall(board):
	board.reverse()
	for i in xrange(len(board)):
		for row,line in enumerate(board):
			for col,char in enumerate(line):
				if char=='.' and row<(len(board)-1):
					board[row][col],board[row+1][col]=board[row+1][col],'.'
	board.reverse()
	return board
	
def transpose(board):
	for i in xrange(len(board)):
		for j in xrange(i):
			board[i][j],board[j][i]=board[j][i],board[i][j]
	return board
	
def make_diagonal(board,k, i,j, delta):
	return ''.join(board[i+num][j+num*delta] for num in xrange(k) if 0<=(i+num)<len(board) and 0<=(j+num*delta)<len(board))

def check(board,k):
	foundR=False
	foundB=False
	rwin='R'*k
	bwin='B'*k
	for row in board:
		s=''.join(row)
		foundR=foundR or rwin in s
		foundB=foundB or bwin in s
	
	for col in xrange(len(board[0])):
		s=''.join(line[col] for line in board)
		foundR=foundR or rwin in s
		foundB=foundB or bwin in s
	
	for i in xrange(len(board)):
		for j in xrange(len(board)):
			diag1=make_diagonal(board,k,i,j,+1)
			diag2=make_diagonal(board,k,i,j,-1)
			#print diag1
			#print diag2
			foundR=foundR or rwin in diag1
			foundB=foundB or bwin in diag1
			
			foundR=foundR or rwin in diag2
			foundB=foundB or bwin in diag2
	return (foundR,foundB)

def pb(board):
	new_board=[''.join(line) for line in board]
	print '\n'.join(new_board)
	
if __name__=='__main__':
	cases=int(stdin.readline())
	for case in xrange(1,cases+1):
		N,K=map(int,stdin.readline().split())
		board=[list(stdin.readline().strip()) for i in xrange(N)]
		#pb(board)
		#
		board=transpose(board)
		#pb(board)
		#print
		board=fall(board)
		#pb(board)
		one,two=check(board,K)
		if one and two:
			answer="Both"
		elif one:
			answer="Red"
		elif two:
			answer="Blue"
		else:
			answer="Neither"
		print "Case #%d: %s"%(case,answer)
