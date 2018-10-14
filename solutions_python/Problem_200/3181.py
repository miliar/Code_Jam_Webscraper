def minus1(c):
	return str(int(c)-1)

def solve(num):
	A = list(num)
	n = len(A)
	s = 0
	for i in xrange(n-1):
		if int(A[i]) < int(A[i+1]):
			s = i+1
		elif int(A[i]) > int(A[i+1]):
			A[s] = minus1(A[i])
			for j in xrange(s+1, n):
				A[j] = '9'
			if A[0] == '0':
				return ''.join(A[1:n])
			return ''.join(A)
	return num

caseNum = int(raw_input())
for i in range(caseNum):
	print 'Case #%d: %s' % (i+1, solve(raw_input()))