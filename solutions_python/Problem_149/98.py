from collections import deque

def min_swaps(A):
	res = 0
	for i in xrange(len(A)):
		for j in xrange(i+1, len(A)):
			if A[j] < A[i]:
				res += 1
	return res

def min_swaps_wut(A, B):
	res = 0
	Bindex = {}
	for i in xrange(len(B)):
		Bindex[B[i]] = i
	for i in xrange(len(A)):
		for j in xrange(i+1, len(A)):
			if Bindex[A[j]] < Bindex[A[i]]:
				res += 1
	return res

def solve(A):
	B = sorted(A)
	ind = A.index(B[-1])
	mval, marr = 10000000, []
	for b in xrange(2**(N-1)):
		arr = deque([B[-1]])
		for i in xrange(len(A)-2, -1, -1):
			if b & (1 << i) > 0:
				arr.append(B[i])
			else:
				arr.appendleft(B[i])
		mn = min_swaps_wut(A, arr)
		if mn < mval:
			mval = mn
			marr = arr
	for i in xrange(ind, 0, -1):
		A[i-1], A[i] = A[i], A[i-1]
	mn, mnarr = 10000000, []
	for i in xrange(len(A)):
		if i > 0:
			A[i-1], A[i] = A[i], A[i-1]
		res = abs(ind - i) + min_swaps(A[:i]) + min_swaps(A[-1:i:-1])
		if res < mn:
			mn = res
			mnarr = A[:]
	return mval

T = int(raw_input())
for test in xrange(1, T+1):
	N = int(raw_input())
	A = map(int, raw_input().split())
	print "Case #" + str(test) + ": " + str(solve(A))
