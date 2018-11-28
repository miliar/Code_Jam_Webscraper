input = '''0
INPUT GOES HERE
'''

lines = input.splitlines()
num = int(lines[0])

from math import *


def check(N, K):

	if K == 0:
		return 'OFF'		
	
	n = floor(log(K)/log(2))
	#~ print N, K, n
	#~ print '--'

	if (n + 1) == N:
		return 'ON'
	elif N > (n + 1):
		return 'OFF'
	else:
		return check(N, K - 2**n)


for K in range(0):
	print K,
	for N in range(1,8):
		r = check(N, K)
		if r == 'ON':
			print '[ ]',
		else:
			print '[X]',
	print


for i in range(num):
	N, K = lines[i+1].split()
	N = int(N)
	K = int(K)
	
	state = 'OFF'
	for nn in range(1, N+1):
		state = check(nn, K)
		if state == 'OFF':
			break
	
	print 'Case #%i: %s'% (i+1, state)


