T = int(raw_input().split()[0])


for t in xrange(T):
	
	N, P = map(int, raw_input().split())

	if P == 2 ** N:
		res1 = 2 ** N - 1
		res2 = 2 ** N - 1
	else:
		shitlist1 = [1]
		shitlist2 = [0]
		x, y = 1, 0
		for i in xrange(N):
			shitlist1.append(x + 2 ** (N-1-i))
			x += 2 ** (N-1-i)
			shitlist2.append(y + 2 ** (i+1))
			y += 2 ** (i+1)
			
		for i in xrange(len(shitlist1)):
			if P < shitlist1[i]:
				res1 = shitlist2[i-1]
				break
			
		shitlist3 = []
		shitlist4 = []
		for i in xrange(N+1):
			shitlist3.append(2 ** (N-i))
			shitlist4.append(2 ** N  - 2 ** (i))
			
		for i in xrange(len(shitlist3)):
			if P >= shitlist3[i]:
				res2 = shitlist4[i]
				break
		
	print "Case #%d: %d %d" % (t+1, res1, res2)