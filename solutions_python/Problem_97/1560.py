for x in range(input()):
	a,b=map(int,raw_input().split())
	res = 0
	for t in range(a,b+1):
		for u in range(t+1,b+1):
			if str(t) in str(u)*2:res+=1
	print "Case #%d: %d" %(x+1,res)
