#fi = open('A-test.in','r')
fi = open('A-large.in','r')
fo = open('A-large.out','w')

T = int(fi.readline().strip())
for t_no in range(1,T+1):
	#print "Case #%d:" % (t_no)
	fo.write("Case #%d: \n" % (t_no))
	N = int(fi.readline().strip())
	sch = []
	listWP = []
	listOWP = []
	listOOWP = []
	for i in range(N):
		team = fi.readline().strip()
		sch.append(team)
	for i in range(N):
		won = list(sch[i]).count('1')
		lose = list(sch[i]).count('0')
		n = won + lose
		WP = float(won)/n
		listWP.append(WP)
		count = 0
		OWP = 0
		for j in range(N):
			if sch[i][j] != '.':
				count += 1
				if sch[i][j] == '1':
					won = list(sch[j]).count('1')
					lose = list(sch[j]).count('0') - 1
					n = won + lose
					x = float(won)/n
				else :
					won = list(sch[j]).count('1') - 1
					lose = list(sch[j]).count('0')
					n = won + lose
					x = float(won)/n
				OWP += x
		OWP = float(OWP)/count
		listOWP.append(OWP)
	for i in range(N):
		count = 0
		OOWP = 0
		for j in range(N):
			if sch[i][j] != '.':
				count += 1
				x = listOWP[j]
				OOWP += x
		OOWP = float(OOWP)/count
		listOOWP.append(OOWP)
	for i in range(N):
		RPI = 0.25*listWP[i] + 0.50*listOWP[i] + 0.25*listOOWP[i]
		fo.write("%.12f\n" % RPI)
	
fi.close()
fo.close()