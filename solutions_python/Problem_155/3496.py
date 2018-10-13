z = int(raw_input())
for i in range(z):

	x = raw_input().split();
	maxs = int(x[0])
	lists = map(int, list(x[1]))
	people = 0
	friends = 0
	for n in range(maxs+1):
		curfriends=0
		if(people<n and lists[n]>0):
			friends+= n-people
			curfriends = friends

		people += lists[n] + curfriends
	print "Case #%d: %d" %(i+1, friends)