#!/usr/bin/python

def avg(lst):
	return sum(lst)/len(lst)

def solve(lines):
	al = [ float(len(line)-line.count('.')) for line in lines ]
	win = [ float(line.count('1'))  for line in lines ]
	wp = [ x/y for x,y in zip(win,al) ]
	owp = [ 0 for x in xrange(len(lines)) ]
	for i in xrange(len(line)):
		owp[i] = avg([ (x - (lines[j][i]=='1'))/(y-1) for x,y,j in zip(win,al,xrange(len(lines))) if lines[j][i]!='.' ])
	oowp = [ avg([ owpi for owpi,j in zip(owp,xrange(len(lines))) if lines[i][j]!='.' ]) for i in xrange(len(lines)) ]	
#	print "wp: ", wp
#	print "owp: ", owp
#	print "oowp: ", oowp
	return [ 0.25*wpi+0.50*owpi+0.25*oowpi for wpi,owpi,oowpi in zip(wp,owp,oowp) ]


T = int(raw_input())
for i in xrange(T):
	N = int(raw_input())
	lines = [ raw_input().strip() for s in xrange(N) ]
	print "Case #%d:" % (i+1)
	print "\n".join( str(i) for i in solve(lines) ).rstrip()
