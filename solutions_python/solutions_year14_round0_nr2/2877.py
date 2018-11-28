T = input()

for t in range(1, T+1):
	c, f, x = map(float, raw_input().split())
	
	time = 0
	farms = 0
	while x/(farms*f+2) > c/(farms*f+2) + x/((farms+1)*f + 2):
		time += c/(farms*f+2)
		farms += 1

	time += x/(farms*f+2)
	
	print "Case #%d: %.7f" % ( t, time )
