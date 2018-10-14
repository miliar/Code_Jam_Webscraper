
import sys
import math
import random

def readstr():
	return sys.stdin.readline().strip()

def readint():
	return int(readstr())

def tolist( stri, delim='' ):
	if delim == '':
		return stri.split()
	else:
		return stri.split( delim )

def readlist( delim='' ): return tolist( readstr(), delim )

def evallist( l, f ):
	v = []
	for i in l:
		v.append( f(i) )
	return v

def readevallist( f, delim='' ):
	return evallist( readlist(delim), f )

def readints( delim='' ): return readevallist( int, delim )

L,D,N = readints()
words = []

for i in range(D):
	words.append( readstr() )

for i in range(N):
	pat = readstr()

	opt = []

	j = 0

	while j < len(pat):
		if pat[j] != '(':
			opt.append( [ pat[j] ] )
		else:
			v = []
			j += 1
			while pat[j] != ')':
				v.append(pat[j])
				j += 1

			opt.append( v )

		j += 1

	pot = range(D)
			
	for kn in range(L):
		v = opt[kn]
		uudet_p = []
		for s in pot:
			if words[s][kn] in v:
				uudet_p.append( s )
		pot = uudet_p

	print "Case #"+str(i+1)+": "+str(len(pot))

