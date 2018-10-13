#!/usr/bin/env python

T = int(raw_input())
for t in xrange(T):
	N = raw_input()
	M = ''
	fill9s = False
	for i in xrange(len(N)-1):
		if fill9s:
			M += '9'
			continue
		if int(N[i]) <= int(N[i+1]):
			M += N[i]
		else:
			M += str(int(N[i])-1)
			for j in xrange(len(M)-1, 0, -1):
				if int(M[j]) < int(M[j-1]):
					M = M[0:j-1] + str(int(M[j-1]) - 1) + '9' + M[j+1:]
				else:
					break
			fill9s = True
	if fill9s: M += '9'
	else: M += N[-1]
	print 'Case #%d: %d' %(t+1, int(M))