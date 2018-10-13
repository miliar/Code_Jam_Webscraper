import sys

def run(D,N,K,S):
	reach = [None] * N
	reach[N-1] = float(D - K[N-1]) / float(S[N-1])
	for i in reversed(xrange(N-1)):
		reach[i] = max(reach[i+1], float(D-K[i]) / float(S[i]))

	#print >>sys.stderr, "reach = " + str(reach)

	return float(D)/float(reach[0])

if __name__ == '__main__':
	T = int(raw_input())
	for t in xrange(T):
		(D,N) = map(int, raw_input().split())

		k = []
		s = []
		for n in xrange(N):
			(K,S) = map(int, raw_input().split())
			k.append(K)
			s.append(S)

		print "Case #%d: %.6f" % (t+1,run(D,N,k,s))
