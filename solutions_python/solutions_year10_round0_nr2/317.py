
def gcd(a, b):
	if b == 0: return a
	if a < b: return gcd(b, a)
	return gcd(b, a%b)

if __name__ == '__main__':
	C = input()
	for _42 in xrange(C):
		N, T = raw_input().split(' ', 1)
		N = int(N)
		T = [int(x) for x in T.split()]
		T.sort()
		T.reverse()

		D = []
		for i in xrange(len(T)):
			for j in xrange(i+1, len(T)):
				D.append(T[i] - T[j])

		G = D[0]
		for i in xrange(1, len(D)):
			G = gcd(G, D[i])
		#print 'G =', G

		y = -T[0] % G

		#print 'y =', y
		#print 'T[0] =', T[0]
		#print 'T[0] % G =', T[0] % G

		print "Case #%d: %d" % (_42+1, y)
