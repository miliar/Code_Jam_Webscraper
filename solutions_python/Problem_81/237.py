def solve(matrix):
	WParray=[]
	Tgames=[]
	for i in range(N):
		wins=0
		loses=0
		byes=0
		for j in range(N):
			if matrix[i][j]=="1":
				wins+=1
			elif matrix[i][j]=="0":
				loses+=1
			else:
				byes+=1
		games=N-byes
		Tgames.append(games)
		WP=1.0*wins/games
		WParray.append(WP)
	
	OWParray=[]
	for team in range(N):
		games=0
		totOpAdjWP=0
		for opp in range(N):
			if matrix[team][opp]==".":
				continue
			won=0
			if matrix[team][opp]=="0":
				won=1
			adjustedWP=(WParray[opp]*Tgames[opp]-won)/(Tgames[opp]-1)
			totOpAdjWP+=adjustedWP
			games+=1
		teamOWP=1.0*totOpAdjWP/games
		OWParray.append(teamOWP)
	#print "WP"
	#print WParray
	#print "OWP"
	#print OWParray
	OOWParray=[]
	for team in range(N):
		games=0
		totOWP=0
		for opp in range(N):
			if matrix[team][opp]==".":
				continue
			totOWP+=OWParray[opp]
			games+=1
		OOWParray.append(1.0*totOWP/games)
	#print "OOWP"
	#print OOWParray
	
	RPI=[OOWParray[i]*0.25+OWParray[i]*0.5+WParray[i]*0.25 for i in range(N)]
	#print "RPI"
	#print RPI
	return RPI

f=open("in.txt")
f_out=open("out.txt",'w')

Tests=int(f.readline().strip())
for case in range(1,Tests+1):
	N=int(f.readline().strip())
	matrix=[]
	for i in range(N):
		matrix.append(f.readline().strip())
	
	RPI=solve(matrix)
	
	#print "Case #%d:\n%s" %(case,str("\n".join([str(i) for i in RPI])))
	
	f_out.write("Case #%d:\n%s\n" %(case,str("\n".join([str(i) for i in RPI]))))
