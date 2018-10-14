from sys import stdin
readline = stdin.readline

T = int(readline())

for t in xrange(1, T+1):
	N = [int(dig) for dig in readline().strip()]
	
	done = False
	while not(done):
		for i in xrange(len(N)-1):
			if N[i] > N[i+1]:
				N[i] -= 1
				for j in xrange(i+1, len(N)):
					N[j] = 9
				break
		else:
			done = True
	
	ans = int(''.join(map(str, N)))
	
	print "Case #%d: %d" % (t, ans)
