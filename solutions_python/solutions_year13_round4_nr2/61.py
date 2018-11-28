#! /Library/Frameworks/Python.framework/Versions/Current/bin/python

def findMaxLosses(N,P):
	for l in range(N+1):
		if 2**(N-l) * (2**l - 1) >= P:
			return l - 1
	return N

def findMinWins(N,P):
	for w in range(N,-1,-1):
		if 2**(N-w) - 1 >= P:
			return w + 1
	return 0

T = int(raw_input())

for t in range(1,T+1):

	inpArr = raw_input().split()

	N = int(inpArr[0])
	P = int(inpArr[1])

	guaranteed = 2**(findMaxLosses(N,P) + 1) - 2
	if guaranteed >= 2**N:
		guaranteed = 2**N - 1
	lucky = 2**N - 2**findMinWins(N,P)

	print 'Case #'+str(t)+': '+str(guaranteed)+' '+str(lucky)