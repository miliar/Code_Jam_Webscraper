f = open("D-large.in")

N = int(f.readline().strip())

for i in range(N):
	f.readline()
	war = 0
	dwar = 0

	girl = map(float, f.readline().strip().split())
	boy = map(float, f.readline().strip().split())
	

	# play war
	girlcopy = sorted([x for x in girl])
	boycopy = sorted([x for x in boy])
	while len(girlcopy):
		g = girlcopy.pop()
		
		if(max(boycopy) < g):
			war += 1
			boycopy = boycopy[1:]

		else:
			boycopy.pop()		


	# play deceitful war
	girl.sort()
	boy.sort()
		
	while len(boy):
		b = boy.pop()
		
		if(max(girl) < b):
			girl = girl[1:]

		else:
			dwar += 1
			girl.pop()
	print "Case #{}: {} {}".format(i+1, dwar, war)

	



