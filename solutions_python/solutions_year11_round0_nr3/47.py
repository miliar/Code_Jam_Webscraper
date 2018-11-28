# -*- coding: utf-8 -*-



T = int(raw_input())

for t in range(1,T+1):
	
	N = int(raw_input())
	cans = [int(w) for w in raw_input().split()]
	
	check = reduce(lambda a,b:a^b, cans)
	if check!=0:
		ans = "NO"
	else:
		cans.sort()
		seans = cans[1:]
		ans = str(sum(seans))
	
	print "Case #{x}: {y}".format(x=t,y=ans)











