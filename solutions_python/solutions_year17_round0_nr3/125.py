#usr/bin/python
from __future__ import division
import sys

fin = open(sys.argv[1], "r")
fout = open("C.out", "w")

def func(n, k):
	#if n == 1 and k == 1:
	#	return (0,0)
	#elif n == 2 and k == 1:
	#	return (1,0)
	if n == 0:
		return (0,0)
	elif k == 1:
		return (n//2, n//2 - 1 + n%2)
	elif n%2  == 1:
		return func(n//2, (k -1 + 1)//2 )
	elif k%2 == 1:
		return func(n//2 - 1, k//2)	
	else:
		return func(n//2, k//2 )
	return

T = int(fin.readline())
for ii in xrange(T):
	n, k = map(int,fin.readline().split(' '))

	out = func(n,k)
	fout.write("Case #" + str(ii+1) + ": " + str(out[0]) + " " + str(out[1]) + "\n")