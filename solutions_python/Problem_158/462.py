#!/usr/bin/env python 
import sys
import os
#'''
dbg = lambda x: sys.stdout.write(str(x)+'\n')
dbg = lambda x: None
#'''
import math
def space(X):
	S = range(1,X) 
	for a in S:
		b= int(math.ceil( float(X)/a ))
		yield sorted((a,b)),(a*b-X)


def solve(X,R,C):
	# configuration: resolvable -> True, G.
	#                           -> Fale, R.
	dbg('')
	T= dict([ ( i, list(space(i)) ) for i in range(0,X+1) ])
	dbg( 'T=' )
	for (k,v) in T.items():
		dbg( (k,'->',v) )
	dbg('')

	y = True
	dbg( ('X=',X,'R=',R,'C=',C) )
	N= R*C
	remains= N - X
	dbg( ('N:',N) )
	dbg( ('remains:',remains) )
	#if remains==0:
	#	return False,'no_space'
	if remains % X != 0:
		return False,'not_enough_ncell'
	#if remains % X != 0:
	#	return False,'no_shape_fit'

	narrow, wide = sorted([R,C]) 	
	dbg( ('narrow;',narrow,'wide:',wide) )
	##
	M = [ ((a,b),r) for ((a,b),r) in space(X) if min(a,b)>narrow  ] 
	dbg( ('M=',M) )	
	if len(M):
		return False,'no_shape_fit'
	##
	S = [ ((a,b),r) for ((a,b),r) in space(X) if a==narrow and r>0 and N-(a*b)+1<X ] 
	dbg( ('S=',S) )	
	if len(S):
		return False,'cut'

	return y,'n/a';

def main():
	if '-t' in sys.argv:
		os.system('cat ./input | ./main.py')
		sys.exit()

	T = int(input())
	for i in range(1,T+1):
		X, R, C = map(int,sys.stdin.readline().split(' '))
		
		#if i!=4: continue;
		y,r = solve(X,R,C)
		#dbg('xrc: %s -> %s'% ( str((X,R,C)), ['RICHARD','GABRIEL'][int(y)] ))
		#dbg('%s <= xrc: %s'% ( ['RICHARD','GABRIEL'][int(y)], str((X,R,C)) ))
		winner = ['RICHARD','GABRIEL'][int(y)]
		conf = '%d x %d = %d, %d'%tuple(sorted([R,C])+[R*C,X])  
		xrc = str((X,R,C))
		dbg('%s <= %s, %s, xrc: %s'% ( winner, r, conf , xrc) )
		print 'Case #%d: %s'%(i,winner)
	return 0

if __name__=='__main__':
	sys.exit(main())
