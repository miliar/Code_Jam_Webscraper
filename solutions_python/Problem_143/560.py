'''
New Lottery Game
'''


if __name__ == '__main__':
	f=open("B-small-attempt0.in")
	nc=int(f.readline())
	for x in xrange(1,nc+1):
		[A,B,K] = map(int, f.readline().strip().split(' '))
		s = 0
		for i in xrange(A):
			for j in xrange(B):
				if (i & j < K):
					s += 1			
		print "Case #%d: %d" % (x, s)
