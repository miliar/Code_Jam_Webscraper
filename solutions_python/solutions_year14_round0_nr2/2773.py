import sys
f = open(sys.argv[1])
N = int(f.readline().strip())
for case in xrange(1,N+1):
	C,F,X = map(float, f.readline().strip().split(" "))
	print "Case #%s:" %(case),
	if X < C:
		print X/2
	else:
		nFarm = 0
		total_time = 0 
		DIFF = X - C
		while True:
			cookie_per_sec = 2 + F*nFarm
			time = C/cookie_per_sec
			total_time += time
			time_if_no_buy = DIFF/cookie_per_sec
			time_if_buy = X/(cookie_per_sec + F)
			if time_if_no_buy < time_if_buy:
				print format(total_time + time_if_no_buy, '.7f')
				break
			nFarm += 1
		
