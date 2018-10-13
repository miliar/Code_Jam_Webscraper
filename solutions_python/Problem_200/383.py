#! /usr/bin/python

T = int(raw_input())

def isTidy(n):
	dMax = 9
	while n > 0:
		d = n % 10
		if d > dMax:
			return False
		dMax = d
		n /= 10
	return True

for t in range(1, T+1):

	N = int(raw_input())

	pwr = 1
	while not isTidy(N):
		N = N - (N % (10 ** pwr)) - 1
		pwr += 1

	print 'Case #' + str(t) + ': ' + str(N)