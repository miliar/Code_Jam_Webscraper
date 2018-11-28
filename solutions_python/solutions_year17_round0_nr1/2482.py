#!/usr/bin/python

def flip(S, K):
	for i in xrange(K):
		if S[i] == '-':
			S[i] = '+'
		else:
			S[i] = '-'
	return S

for tc in xrange(1, int(raw_input()) + 1):
	print 'Case #%d:' % (tc),
	S, K = raw_input().split()
	S = list(S)
	K = int(K)
	flag = True
	flip_count = 0
	# print S, K
	for i in xrange(len(S)):
		if S[0] == '-':
			if len(S) >= K:
				S = flip(S, K)
				flip_count += 1
			else:
				flag = False
				break
		# print S
		S = S[1:]
	if flag:
		print flip_count
	else:
		print "IMPOSSIBLE"
