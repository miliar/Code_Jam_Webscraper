from sys import stdin

T = int(stdin.readline())
for c in xrange(1, T+1):
	a = []
	R, k, N = stdin.readline().split()
	R = int(R)
	k = int(k)
	N = int(N)
	gs = stdin.readline().split()
	for i in xrange(len(gs)):
		gs[i] = int(gs[i])
	start = 0
	counter = 0
	ret = 0
	for xxx in xrange(R):
		sum = 0
		cnt = 0
		for i in xrange(len(gs)):
			if sum + gs[(i+start)%len(gs)] <= k:
				sum += gs[(i+start)%len(gs)]
				cnt += 1
			else: 
				break
		a.append(sum)
		ret += sum
		start = (start+cnt)%len(gs)

	#print counter
	#print a
	#print ret

	print "Case #" + str(c) + ": " + str(ret)
