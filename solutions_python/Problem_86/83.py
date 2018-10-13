T = int(raw_input())

for t in range(T):
	N,L,H = map(lambda x: int(x), raw_input().split(" "))
	arr = map(lambda x: int(x), raw_input().split(" "))

	found = False	
	for i in range(L,H+1):
		possible = True
		for j in arr:
			if j % i != 0 and i % j != 0:
				possible = False
		
		if possible == True:
			found = True
			break
	
	if found:
		print "Case #%d: %d" % (t+1, i)
	else:
		print "Case #%d: NO" % (t+1)