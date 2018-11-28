T = input()
for test in xrange(1,T+1):
	smax,max_a = raw_input().split()
	smax=int(smax)
	numStanding = 0
	invites = 0
	for i in xrange(0,smax+1):
		x = int(max_a[i])
		if i>numStanding:
			invites+=i-numStanding
			numStanding+=i-numStanding+x
		else:
			numStanding+=x
	print "Case #"+str(test)+":",invites


