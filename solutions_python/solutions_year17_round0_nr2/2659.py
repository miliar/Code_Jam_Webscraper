#!/usr/bin/python

def tidy(N):
	prev_n = 0
	for curr_n in str(N):
		curr_n = int(curr_n)
		if prev_n > curr_n:
			return False
		prev_n = curr_n
	return True

for tc in xrange(1, int(raw_input()) + 1):
	# N = int(raw_input())
	# while N > 0:
	# 	if tidy(N):
	# 		break
	# 	N -= 1
	# print 'Case #%d:' % (tc), N
	N = map(lambda x: int(x), raw_input())
	prev_n = 0
	for i in xrange(len(N)):
		if prev_n > N[i]:
			N[i - 1] -= 1
			j = i - 1
			while j > 0 and N[j] < N[j - 1]:
				N[j - 1] -= 1
				N[j] = 9
				j -= 1
			while i < len(N):
				N[i] = 9
				i += 1
			break
		prev_n = N[i]
	print 'Case #%d:' % (tc),
	print int(''.join(str(k) for k in N))
