import sys

def solve(A):
	f = 0
	sum = 0
	for i in range(len(A)):
		if A[i] > 0 and sum < i:
			f += i - sum
			sum = i
		sum += A[i]
	return f

T = int(raw_input())

for tc in range(T):
	r = raw_input()
	s = r.split()
	N = int(r[0])
	A = []
	for i in range(N+1):
		A.append(int(s[1][i]))
	print "Case #{:d}: {:d}".format(tc+1, solve(A))