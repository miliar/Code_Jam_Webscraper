import sys

def flip(x):
	return {"+": "-", "-": "+"}[x]

def run(S,K):
	n = 0
	for i in xrange(len(S)-K+1):
		if S[i] == "-":
			for j in xrange(K):
				S[i+j] = flip(S[i+j]);
			n += 1

	return "IMPOSSIBLE" if set(S) != {"+"} else n

if __name__ == '__main__':
	T = int(raw_input())
	for t in xrange(T):
		(S,K) = raw_input().split()
		S = list(S)
		K = int(K)
		print "Case #%d: %s" % (t+1, run(S,K))
		#print "Case #%d: %s" % (t+1, brute(S,K))
