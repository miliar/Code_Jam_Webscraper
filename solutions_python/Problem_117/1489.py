from sys import stdin
import numpy as np




f = open('B-small-attempt0.txt','w')
stdin = open('B-small-attempt0.in', 'r')
T = int(stdin.next().strip())
for t in xrange(1,T+1):
	N, M = map(int, stdin.next().split())
	pattern = np.array([map(int, stdin.next().split()) for i in xrange(N)])
	lawn = np.empty([N,M])
	
	for i in range(N):
		lawn[i,:] = np.max(pattern[i,:])
	
	for j in range(M):
		if not (lawn[:,j] == pattern[:,j]).all():
			lawn[:,j] = np.max(pattern[:,j])
		
	result = 'NO'
	
	if (lawn == pattern).all():
		result = 'YES'
		
	#print 'Case #%d: %s' % (t, result)			
	f.write("""Case #"""), f.write(str(t)), f.write(": "), f.write(str(result)), f.write("\n")

f.close()	