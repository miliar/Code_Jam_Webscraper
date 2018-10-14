#!/usr/bin/python

f = open('B-small-attempt0.in')
#f = open('b-input.in')
inputline = f.readline()
numcase = int(inputline)

fout = open('b_small_result.txt', 'w')
#fout = open('b_test_result.txt', 'w')
dlist = []

def findmax(list):
	lenlist = len(list)
	best=list[0]
	bestpos = 0
	for i in range(lenlist-1,-1,-1):
		if list[i] > best:
			best = list[i]
			bestpos = i
	list[bestpos] = -1
	return bestpos

for i in range (0,numcase):
	line = f.readline()
	linelist = line.split()
	numboost = int(linelist[0])
	btime = int(linelist[1])
	n = int(linelist[2])
	c = int(linelist[3])
	jtime = 0
	tsaved = []
	est_time = []
	cumdist = []
	dlist = []
	#print "n=",n," C=",c
	for j in range (4,c+4):
		#print " add new dist=",linelist[j]
		dlist.append(int(linelist[j]))
	
	for j in range (c,n):
		dlist.append(dlist[j-c])
	
	if numboost == 0:
		totaldist = 0
		for j in range (0,n):
			totaldist = totaldist + dlist[j]
		jtime = totaldist * 2
	elif numboost == n:
		totaldist = 0
		jtime = 0
		for j in range (0,n):
			if jtime >= btime:
				#boost exist for whole leg
				jtime = jtime + (dlist[j])
			elif (jtime + (dlist[j]*2)) < btime:
				jtime = jtime + dlist[j]*2
			else:
				#available halfway
				b_off = btime - jtime
				no_boost_dist = 0.5 * b_off
				rem_dist = dlist[j] - no_boost_dist
				jtime = jtime + b_off + rem_dist
	else:
		cumdist.append(0)
		for j in range (1,n):
			cumdist.append(cumdist[j-1] + dlist[j-1])
		for j in range (0,n):
			#print "##########timesaved calc"
			timesaved = 0
			timereq = cumdist[j] * 2
			endtime = dlist[j] * 2
			if timereq > btime:
				timesaved = dlist[j]
			elif btime > (endtime + timereq):
				timesaved = 0
			else:
				#available halfway
				b_off = btime - timereq
				no_boost_dist = 0.5 * b_off
				rem_dist = dlist[j] - no_boost_dist
				timesaved = rem_dist
				#print "### b_off=",b_off," no_boost_dist=",no_boost_dist
				
			tsaved.append(timesaved)
		boostlist =[]
		mod_tsaved = tsaved[:]
		for j in range(0,numboost):
			#pick largest savings
			bestboost = findmax(mod_tsaved)
			boostlist.append(bestboost)
			#print " boost pos=",bestboost
		jtime = 0
		for j in range(0,n):
			#print " dlist[",j,"]=",dlist[j]
			if j in boostlist:
				#print "   tsaved=",tsaved[j]
				jtime = jtime + (dlist[j]*2) - tsaved[j]
			else:
				jtime = jtime + (dlist[j]*2)
			#print " j=",j," jtime=",jtime
	answer = "Case #"+str(i+1)+": "+str(int(jtime))		
	print answer
	fout.write(answer)
	fout.write('\n')

