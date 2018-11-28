def solve():
	t = int(raw_input())
	for case in xrange(1,t+1):
		n,l,h = raw_input().split()
		n = int(n)
		l = int(l)
		h = int(h)
		f = map(int,raw_input().split())
		answer = -1
		for test in xrange(l,h+1):
			possible = True
			for p in f:
				if p % test != 0 and test % p != 0:
					possible = False
					break
			if possible == True:
				answer = test
				break
		if answer == -1:
			print "Case #" + str(case) + ": NO"
		else:
			print "Case #" + str(case) + ": " + str(test)

solve()
