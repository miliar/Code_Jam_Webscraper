def WP(i, team):
	count = 0.0
	t = 0
	for c in team:
		if c == '1':
			count = count + 1
		if c != '.':
			t += 1
	return count / t

def getowp(i, teams):
	sum = 0.0
	count = 0
	for j in xrange(N):
		if j != i:
			if teams[i][j] != '.':
				sum = sum + WP(j, teams[j][:i] + teams[j][i+1:])
				count += 1
	return sum/count
	
def getoowp(i,teams):
	sum = 0.0
	count = 0
	for j in xrange(N):	
		if j != i:
			if teams[i][j] != '.':
				sum = sum + owp[j]
				count += 1
	return sum/count
	
for casenum in xrange(1,1+int(raw_input())):
	N = int ( raw_input())
	teams = []
	ans = ''
	for i in xrange(N):
		teams.append(raw_input())
	wp = []
	owp = []
	oowp = []
	owplist = []
	RPI = []
	for i in xrange(N):
		wp.append( WP(i,teams[i]) )
	for i in xrange(N):	
		owp.append(getowp(i,teams))
	for i in xrange(N):
		oowp.append(getoowp(i,teams))
	for i in xrange(N):
		RPI.append(0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i])
	print ("Case #%d: " % casenum)
	for i in xrange(N):
		print(RPI[i])