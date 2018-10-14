# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:39:53 2016

@author: aanderson
"""

T = int(raw_input())
for i in xrange(1, T + 1):
	N = raw_input()
#	N = N[::-1]
#	print(N)
	if len(N) > 1:
		for m in range(len(N))	:
#			print(N)
			idx = -1
			for n in range(len(N)-1):
				idx = idx + 1
#				print(int(N[n]), int(N[n+1]))
				if int(N[n]) > int(N[n+1]):
					break
#			print(N,n,idx)	
			if int(N[n]) > int(N[n+1]):
				l = list(N)
				l[n] = str((int(l[n])-1)%10)
				l[n+1:] = ['9']*len(l[n+1:])
				N = ''.join(l)
	
#	N = N[::-1]
	while N[0] == '0':
		l = list(N)
		l = l[1:]
		N = ''.join(l)
	
	print "Case #{}: {}".format(i, N)