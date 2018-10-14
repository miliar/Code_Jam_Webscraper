T = int(raw_input())

# given a matrix, compute winning percentage
#  not considering the ignore element
def wp(A,team,ignore):
	wins, losses = 0, 0
	resultline = A[team]
	for team in range(len(resultline)):
		if team == ignore or resultline[team] == '.': continue
		if resultline[team] == '1': wins += 1
		if resultline[team] == '0': losses += 1
	return float(wins) / (wins+losses)

# compute avg winning percentage of opponents	
def owp(A,team):
	resultline = A[team]
	nOpponents = 0
	total = 0.0
	for opp in range(len(resultline)):
		if opp == team or resultline[opp] == '.': continue
		total += wp(A,opp,team)
		nOpponents += 1
	return total / nOpponents

def oowp(A,team):
	resultline = A[team]
	nOpponents = 0
	total = 0
	for opp in range(len(resultline)):
		if opp == team or resultline[opp] == '.': continue
		total += owp(A,opp)
		nOpponents += 1
	return total / nOpponents
	
for case in range(1,1+T):
	N = int(raw_input())
	A = []
	for team in range(N):
		line = raw_input()
		A.append(line)

	print "Case #%d:" % case
	
	for team in range(N):
		WP = wp(A,team,team)
		OWP = owp(A,team)
		OOWP = oowp(A,team)

	#print "(WP, OWP, OOWP) = %f, %f, %f" % (WP,OWP,OOWP)
		RPI = .25*WP + .5*OWP + .25*OOWP
		print RPI
	
