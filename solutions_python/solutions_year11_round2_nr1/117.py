T = int(raw_input())

wp = []
owp = []
oowp = []

def WP(team, ex = None):
	total_played = 0
	total_won = 0
	for j in range(N):
		if j == ex: continue
		if arr[team][j] == '.': continue
		else:
			total_played += 1
			if arr[team][j] == '1': total_won += 1	
	return float(total_won)/total_played
	
def OWP(team, ex = None):
	total_owp = 0
	total_owp_count = 0		
	
	for j in range(N):
		if j != team and arr[j][team] != '.':
			total_owp += WP(j, team)
			total_owp_count += 1	
			
	return float(total_owp)/(total_owp_count)		

def OOWP(team):
	total_oowp = 0
	total_oowp_count = 0		
	
	for j in range(N):
		if j != team and arr[j][team] != '.':
			total_oowp += owp[j]
			total_oowp_count += 1	
			
	return float(total_oowp)/(total_oowp_count)		
		

for t in range(T):
	N = int(raw_input())
	arr = []
	for i in range(N):
		arr.append(raw_input())	
	
	wp = []
	owp = []
	oowp = []
	for i in range(N):
		wp.append(WP(i))
		owp.append(OWP(i))

	for i in range(N):
		oowp.append(OOWP(i))

	

	print "Case #%d:" % (t+1)
	for i in range(N):
		print 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]