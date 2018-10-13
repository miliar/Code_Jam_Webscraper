T = input()
for j in xrange(T):
	A, B, K = [int(i) for i in raw_input().split()]
	count = 0 
	for k in xrange(A):
		for l in xrange(B):
			if k&l < K :
				count+=1

	print "Case #%d: %d"  %(j+1, count)
	


