#! /usr/bin/python
from sys import stdin, setrecursionlimit as recdepth
from cStringIO import StringIO 

d=[(-1,0),(0,-1),(0,+1),(+1,0)]
recdepth(100000)
def get_sink(r,c,board, colour, comp):
	if colour[r][c]>-1:
		return colour[r][c]
	cand=[]
		
	for i,x in enumerate(d):
		nr=r+x[0]
		nc=c+x[1]
		if nr>=0 and nr<len(board) and nc>=0 and nc<len(board[0]) and board[nr][nc]<board[r][c]:
			#colour[r][c]=get_sink(nr,nc,board,colour, comp)
			#return colour[r][c]
			cand.append((board[nr][nc],i,nr,nc))
	cand.sort()
	
	if len(cand):
		x=cand[0]
		colour[r][c]=get_sink(x[-2],x[-1],board,colour,comp)
	else:
		colour[r][c]=chr(comp[0]+ord('a'))
		comp[0]+=1
	return colour[r][c]
	
if __name__=='__main__':
	data=StringIO(stdin.read())
	T=int(data.readline())
	for case in xrange(1,T+1):
		H,W=map(int,data.readline().split())
		board=[map(int,data.readline().split()) for i in xrange(H)]
		colour=[[-1]*W for i in xrange(H)]
		comp=[0]
		for r in xrange(H):
			for c in xrange(W):
				get_sink(r,c,board,colour,comp)
		print "Case #%d:"%case
		colour=[" ".join(line) for line in colour]
		print "\n".join(colour)
