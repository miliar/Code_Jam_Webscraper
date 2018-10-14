import sys

def lastTidy(N):
	n = [int(d) for d in str(N)]
	for i in xrange(len(n)-1,0,-1):
		if n[i] < n[i-1]:
			for j in xrange(i,len(n)):
				n[j] = 9
			n[i-1] = n[i-1]-1
	return int(''.join([str(j) for j in n]))

T = int(sys.stdin.readline())
for i in xrange(1,T+1):
	N = int(sys.stdin.readline())
	x = lastTidy(N)
	print 'Case #' + str(i) + ': ' + str(x)
