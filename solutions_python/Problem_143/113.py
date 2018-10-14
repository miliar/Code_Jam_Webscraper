inf = open('B-large.in', 'r')
outf = open('out.txt', 'w')

for q in xrange(int(inf.readline().strip())):
	A, B, K = [int(i) for i in inf.readline().strip().split()]
	count = 0

	if A <= K or B <=K:
		count = A*B
	else:
		count = K*K + (A-K) * K + (B-K) * K
		for i in range(K, A):
			for j in range(K, B):
				if i & j < K:
					count += 1


	outf.write('Case #%d: %s\n' % (q+1, str(count)))
