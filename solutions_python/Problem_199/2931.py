def flip(c):
	if c == '+': return '-'
	return '+'

def solve(s, K):
	A = list(s)
	n = len(A)
	count = 0
	for i in xrange(n):
		if A[i] == '-':
			if i+K > n:
				return 'IMPOSSIBLE'
			count += 1
			for j in xrange(K):
				A[i+j] = flip(A[i+j])
	return str(count)

caseNum = int(raw_input())
for i in range(caseNum):
	line = raw_input().split()
	s = line[0]
	K = int(line[1])
	print 'Case #%d: %s' % (i+1, solve(s, K))