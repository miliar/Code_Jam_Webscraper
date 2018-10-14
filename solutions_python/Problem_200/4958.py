def function(N):
	flag = False
	for j in xrange(N, 0, -1):
		listN = list(str(j))
		if len(listN) == 1:
			return j
		
		for d in xrange(1, len(listN)):
			if(int(listN[d-1]) > int(listN[d])):
				break
			if d == len(listN)-1:
				flag = True

		if flag:
			return j


T = int(raw_input())

for i in xrange(1,T+1):
	N = int(raw_input())

	print "Case #{}: {}".format(i, function(N))


