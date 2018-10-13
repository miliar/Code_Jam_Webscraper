from collections import deque


def flip(curr, i, k):
	result = list(curr)
	for n in xrange(i, i+k):
		if result[n] == '+':
			result[n] = '-'
		else:
			result[n] = '+'
	return ''.join(result)


n = int(raw_input())
for i in xrange(n):
	s, k = raw_input().split()
	k = int(k)
	
	result = 'IMPOSSIBLE'
	for x in xrange(len(s)):
		#print s
		if '-' not in s:
			result = str(x)
			break

		for y in xrange(len(s) - k+1):
			if s[y] == '-':
				s = flip(s, y, k)
				break


	print 'Case #' + str(i+1) +': ' + result