for case in xrange(input()):
	r,k,n = map(int, raw_input().split())
	g = map(int, raw_input().split())
	assert(len(g) == n)
	
	#solve
	run = 0
	pos = 0
	money = 0
	
	last = [None]*n

	while run < r:
		if last[pos]:
			lastrun, lastmoney = last[pos]
			diffrun = run - lastrun
			diffmoney = money - lastmoney
			runsleft = r-run
			
			loops = (r - run)/diffrun
			if loops:
				run += loops*diffrun
				money += loops*diffmoney
				continue

		last[pos] = (run, money)
		p = 0
		origpos = pos
		while p + g[pos] <= k:
			p +=  g[pos]
			pos = (pos+1)%n
			if pos == origpos:
				break		
		money += p
		run += 1
	
	print "Case #%d:"%(case+1), money