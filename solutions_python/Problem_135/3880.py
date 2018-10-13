#!/usr/bin/python 
import sys


if __name__=='__main__':
		
	T= int( sys.stdin.readline() )
	for i in xrange(1,T+1):
		M= set(range(1,16+1))
		y= 'Bad magician!'
		for j in xrange(2):
			g= int( sys.stdin.readline() )
			C= [ map(int,sys.stdin.readline().split()) for _ in xrange(4) ]
			#
			en0= len(M)
			M= set( C[g-1] ) & M
			en1= len(M)
			#
			if en1 == 1: y= M.pop()
			elif en1 == 0: y= 'Volunteer cheated!'
		print 'Case #%d: %s' % (i,y);
  
