#!/usr/bin/env python
# Python 2.6.x plus (possibly) the following non-standard libraries
#   numpy -- http://numpy.scipy.org/
#   scipy -- http://www.scipy.org/
# input from stdin, output to stdout   -- or --  progname.py input output  -- or --  progname.py input

import os
import sys
import numpy as np

def debug(*x,**a):
	sys.stderr.write("DEBUG: %s\n" % " ".join(concat((repr(v) for v in x),(" ".join("%s=%s" % (k,repr(v)) for (k,v) in a.iteritems())))))

def read_ints():
	return [int(x) for x in raw_input().strip().split()]

def main():
	[N_CASES]=read_ints()
	for case in xrange(1,N_CASES+1):
		[N,K]=read_ints()
		a=np.array([list(raw_input().strip()) for _ in range(N)]).transpose()
#		print K
#		print a
		for i in xrange(N):
			dst=N-1
			src=N-1
			while dst>=0 and a[dst,i]!='.':
				dst-=1
				src-=1
			while src>=0:
				if a[src,i]!='.':
					a[dst,i]=a[src,i]
					if src!=dst:
						a[src,i]='.'
					dst-=1
				src-=1
				
#		print a
		winR=False
		winB=False
		# horiz
		for row in xrange(N):
			tR=0
			tB=0
			for col in xrange(N):
				if a[row,col]=='R':
					tR+=1
					tB=0
				elif a[row,col]=='B':
					tR=0
					tB+=1
				else:
					tR=0
					tB=0
				if tR==K:
					winR=True
				if tB==K:
					winB=True
		# vert
		for col in xrange(N):
			tR=0
			tB=0
			for row in xrange(N):
				if a[row,col]=='R':
					tR+=1
					tB=0
				elif a[row,col]=='B':
					tR=0
					tB+=1
				else:
					tR=0
					tB=0
				if tR==K:
					winR=True
				if tB==K:
					winB=True
		# diag down
		for rowS in xrange(N-K+1):
			for colS in xrange(N-K+1):
				tR=0
				tB=0
				for D in xrange(N-max(rowS,colS)):
					row=rowS+D
					col=colS+D
					if a[row,col]=='R':
						tR+=1
						tB=0
					elif a[row,col]=='B':
						tR=0
						tB+=1
					else:
						tR=0
						tB=0
					if tR==K:
						winR=True
					if tB==K:
						winB=True
		# diag up
		for rowS in xrange(N-K+1):
			for colS in xrange(N-K+1):
				tR=0
				tB=0
				for D in xrange(N-max(rowS,colS)):
					row=N-rowS-D-1
					col=colS+D
					if a[row,col]=='R':
						tR+=1
						tB=0
					elif a[row,col]=='B':
						tR=0
						tB+=1
					else:
						tR=0
						tB=0
					if tR==K:
						winR=True
					if tB==K:
						winB=True
		if winR and winB:
			print "Case #%d: Both" % (case,)
		elif winR:
			print "Case #%d: Red" % (case,)
		elif winB:
			print "Case #%d: Blue" % (case,)
		else:
			print "Case #%d: Neither" % (case,)
			
### run main

if __name__=='__main__':
	main()
