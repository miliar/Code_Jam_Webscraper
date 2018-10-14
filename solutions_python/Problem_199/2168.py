#!/usr/bin/python

import sys

def flip(st,i,k):
	s = list(st)
	if len(s)-i < k:
		return -1
	for j in xrange(k):
		if s[i] == '+':
			s[i] = '-'
		else:
			s[i] = '+'
		i = i+1
	return "".join(s)

T = int(sys.stdin.readline())
for i in xrange(1,T+1):
	flips = 0
	st = sys.stdin.readline()
	[st,K] = st.split(' ')
	K = int(K)
	for j in xrange(len(st)):
		if st[j] == '-':
			st = flip(st,j,K)
			flips = flips+1
			if st == -1:
				break
	if st == -1:
		print 'Case #' + str(i) + ': ' + 'IMPOSSIBLE'
	else:
		print 'Case #' + str(i) + ': ' + str(flips)
