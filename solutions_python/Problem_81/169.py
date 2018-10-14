from __future__ import division
import sys, string
import itertools

def readlist():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

T = int(sys.stdin.readline())

A = [];
N = 0;

def WP(i):
	line = A[i]
	w = len([x for x in line if x == '1'])
	l = len([x for x in line if x == '0'])
	#~ print i, w, l, line
	try: ans = w / (w + l)
	except: ans = 0
	#~ print "WP(%d) = %g" % (i, ans)
	return ans

def WPx(i, you):
	line = list(A[i])
	line[you] = '.'
	w = len([x for x in line if x == '1'])
	l = len([x for x in line if x == '0'])
	#~ print i, you, line, w, l
	try: ans = w / (w + l)
	except: ans = 0
	#~ print "WPx(%d,%d) = %g" % (i, you, ans)
	return ans

owp = {}
def OWP(i):
	
	if i in owp: return owp[i]
	
	s = 0
	n = 0
	for k in range(N):
		#~ print i,k,A[i],A[i][k]
		if A[i][k] != '.':
			s += WPx(k, i)
			n += 1
	try: s /= n
	except: s = 0
	owp[i] = s
	print >> sys.stderr, "OWP(%d) = %g" % (i, s)
	return s

def OOWP(i):
	s = 0
	n = 0
	for k in range(N):
		if A[i][k] != '.':
			s += OWP(k)
			n += 1
	try: s /= n
	except: s = 0
	return s

def RPI(i):
	return 0.25 * WP(i) + 0.50 * OWP(i) + 0.25 * OOWP(i)

for t in range(T):
	N = int(sys.stdin.readline())
	print >> sys.stderr, t, N
	A = []
	owp = {}
	for i in range(N):
		l = sys.stdin.readline().strip()
		A.append(l)
	#~ print A
	
	#~ for i in range(N):
		#~ print "oowp(%g) = %g" % (i, OOWP(i))
	
	print "Case #%d:" % (t+1)
	for i in range(N):
		print RPI(i)
