# Andy Rock
# April 7, 2016
# 
# Qualification Round 2017: Problem B. 

for T in xrange(1, int(input()) + 1):

	N = [int(s) for s in raw_input()][::-1]
	for i in xrange(len(N) - 1):
		if N[i] < N[i + 1]:
			N[i + 1] -= 1
			for j in xrange(i, -1, -1):
				N[j] = 9

	print 'Case #%d: %s' % (T, ''.join(map(str, filter(lambda x : x, N[::-1]))))
