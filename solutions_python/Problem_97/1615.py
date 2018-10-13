
def checker(N, M, A, B):
	if (int(N) < int(M) <= int(B)):
		#print ( N, int(M), A, B)
		return True
	else:
		return False





def counter(A, B):
	corr = set()
	for index in xrange(int(A), int(B)):
		taker = str(index)
		for length in xrange(len(taker)):
			N = taker 
			M = taker[length:] + taker[:length]
			if checker( N, M, A, B ):
				corr.add((N,M))		
	return len(corr)






TEST_CASES = raw_input()

for cases in  xrange(int(TEST_CASES)):
	data = raw_input().split()
	A = data[0]
	B = data[1]

	pr = counter(A, B)
	pri = cases + 1
	print("Case #" + str(pri) + ": " + str(pr))
