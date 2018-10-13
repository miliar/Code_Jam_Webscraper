t = int(raw_input())
for l in xrange(1,t+1):
	n, k = [x for x in raw_input().strip().split(" ")]
	k = int(k)
	n = list(n)
	flips = 0
	# print n
	for i in range(len(n)-k+1):
		if n[i] == '-':
			for j in range(i, i+k):
				if n[j] == '-':
					n[j] = '+'
				else:
					n[j] = '-'
			flips += 1
		# print n
	result = str(flips)
	for i in range(len(n)-k, len(n)):
		if n[i] == '-':
			result = "IMPOSSIBLE"
	print "Case #{}: {}".format(l,result)