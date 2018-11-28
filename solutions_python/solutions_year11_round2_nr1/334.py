f = open("a.in")
n = int(f.readline())
for i in range(0, n): #f or each test case
	print "Case #" +  str(i+1) + ":"
	teams = int(f.readline())
	games = []
	wps = []
	opps = []
	for j in range(0, teams): # for each team
		o = []
		sched = list(f.readline().strip())
		games.append(sched)
		count = 0
		wins  = 0
		for k, game in enumerate(sched):
			if game == '.':
				continue
			count = count + 1
			o.append(k)
			if game == '1':
				wins = wins + 1
		opps.append(o)
		wps.append( (wins, count) )
	owps = []
	for p, op in enumerate(opps): # each team
		tally = 0
		for o in op: # each list of opponenents
			owp = wps[o] # get the winning percent
			g =  games[p][o]
			if ( g == '0' ):
				nowp = (owp[0]-1, owp[1] - 1)
			else:
				nowp = ( owp[0], owp[1] - 1)
			newtotal = float(nowp[0]) / float(nowp[1])
			tally = tally + newtotal
		result = tally / len(op)
		owps.append(result)
	oowps = []
	for m, op in enumerate(opps):
		tally = 0
		for o in op:
			tally = tally + owps[o]
			#print tally
		l = float(len(op))
		#print tally,
		tally = float(tally) / l
		final = ( ( float(wps[m][0])/float(wps[m][1])) * .25) + (owps[m] * .5) + (tally * .25)
	#	print float(wps[m][0])/float(wps[m][1]),owps[m], tally
		print final

			
		
				 
			
		
