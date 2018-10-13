import os
from sys import *
import numpy

T = int(stdin.readline())
for t in xrange(T):
	S, N = stdin.readline().split()
	N = int(N)
	# print S, type(S)
	# print N, type(N)
	# change - to 0, + to 1
	num = []
	for s in S:
		if s == '+':			
			num.append(1)
		elif s == '-':		
			num.append(0)
	num = numpy.asarray(num)	
	flip = 0
	i = 0
	while len(num) > 0:
		if num[0] == 1:
			num = numpy.delete(num,0)			
		elif num[0]==0:
			if len(num) < N:
				flip = 'IMPOSSIBLE'
				break
			elif len(num) >= N:
				num = numpy.concatenate((~num[0:N]+2,num[N:len(num)]))
				flip += 1		
	flip = str(flip)
	print "Case #%s:" %(t+1), flip