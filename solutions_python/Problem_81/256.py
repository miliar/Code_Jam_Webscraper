#!/usr/bin/python

f = open('A-large.in')
#f = open('rpi-input.in')
inputline = f.readline()
numcase = int(inputline)

#fout = open('rpi_small_result.txt', 'w')
fout = open('rpi_large_result.txt', 'w')

records = []
wp=[]
numgames=[]
owp=[]
oowp=[]

for i in range (0,numcase):
	line = f.readline()
	n = int(line)
	teamr=[]
	records = []
	wp=[]
	wongames=[]
	numgames=[]
	owp=[]
	rpi = []
	oowp=[]
	for j in range (0,n):
		line = f.readline()
		gplayed = 0
		wins = 0.0
		thisrec = []
		for k in range (0,n):
			if line[k] == '.':
				thisrec.append(-1)
			elif line[k] == '1':
				thisrec.append(int(line[k]))
				gplayed = gplayed + 1
				wins = wins + 1
			else:
				thisrec.append(int(line[k]))
				gplayed = gplayed + 1
		teamr.append(thisrec)
		#print " wins=",wins," gplayed=",gplayed
		wongames.append(wins)
		numgames.append(gplayed)
		wp.append(wins/gplayed)

	#OWP
	for j in range(0,n):
		temp_owp = 0.0 
		opp_owp = 0.0
		#print " size teamr=",len(teamr)," size teamr[0]=",len(teamr[0])
		for k in range(0,n):
			if (j==k) or  (teamr[j][k] < 0):
				continue;
			else:
				if (teamr[k][j] > 0):
					opp_owp = opp_owp + ((wongames[k]-1) / (numgames[k] - 1.0)) 
				else:
					opp_owp = opp_owp + ((wongames[k]) / (numgames[k] - 1.0)) 
		temp_owp = opp_owp / numgames[j] 
		owp.append(temp_owp)

	#OOWP
	for j in range(0,n):
		temp_oowp = 0.0
		opp_oowp = 0.0
		#print " size teamr=",len(teamr)," size teamr[0]=",len(teamr[0])
		for k in range(0,n):
			if (j==k) or  (teamr[j][k] < 0):
				continue;
			else:		
				opp_oowp = opp_oowp + owp[k] 
		temp_oowp = opp_oowp / numgames[j]	
		oowp.append(temp_oowp)
 	#RPI
	for j in range (0,n):
		newrpi = (0.25 * wp[j]) + (0.50 * owp[j]) + (0.25 * oowp[j])
		rpi.append(newrpi)

	answer = "Case #"+str(i+1)+":"
	print answer
	fout.write(answer)
	fout.write('\n')
	for j in range(0,n):
		answer = str(rpi[j]) 
		print answer
		fout.write(answer)
		fout.write('\n')
