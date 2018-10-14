for t in xrange(int(raw_input())):
	num_teams = int(raw_input())
	l = []
	for i in xrange(num_teams):
		l.append(raw_input())

	WP = []
	OWP = []
	OOWP = []
	
	num_games = len(l[0])
	win = 0
	loss = 0
	for i in xrange(len(l)):
		for game in l[i]:
			if game == '1':
				win+=1
			elif game == '0':
				loss+=1

		WP.append(win/(win+loss+0.0))
		win = 0
		loss = 0
	
	win = 0
	loss = 0
	
	c = list(l) #copy list
	
	temp = []
	
	count = 0
	
	for k in xrange(len(c)): #for every team

		for j in xrange(len(c)): #for every other team team
			if j !=k and c[j][k] != '.': #that is not this one
				for i in xrange(num_games): #for every match
					if c[j][k] != '.':
						if i !=k and (c[j][k] != '.'):
							if c[j][i] == '1':
								win+=1
							elif c[j][i] == '0':
								loss+=1
					#temp.append(win/(win+loss+0.0))
				#print temp

				temp.append(win/(win+loss+0.0))
				#OWP.append(sum(temp)/(count+0.0)) #sum opponent wins/append average for this team
				win = 0
				loss = 0

		OWP.append(sum(temp)/(len(temp)+0.0)) #sum opponent wins/append average for this team
		temp = []

		temp = []
		
	for j in xrange(len(c)):
		for k in xrange(len(c)):
			if k != j and c[k][j] != '.':
				#print 'append',OWP[j]
				temp.append(OWP[k])
		OOWP.append(sum(temp)/(len(temp)+0.0))
		temp = []
			
	#print 'OOWP',OOWP
	print 'Case #'+str((t+1))+':'
	for i in xrange(len(WP)):
		print WP[i]*.25+OWP[i]*.5+OOWP[i]*.25