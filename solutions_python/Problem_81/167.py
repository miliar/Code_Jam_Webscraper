#!/usr/bin/python
import sys

infile = open(sys.argv[1], 'r')

numCases = int(infile.readline())
caseNum = 0

for case in range(numCases):
	caseNum += 1
	
	numTeams = int(infile.readline())
	
	data = []
	
	for i in range(numTeams):
		a = infile.readline()
		data.append(a.rstrip())
	
	wp = []
	for team in data:
		wins = 0
		losses = 0
		for j in team:
			if j == '1':
				wins += 1
			elif j == '0':
				losses += 1
		wp.append(wins / float(wins + losses))
	
	owp = []
	for i in range(numTeams):
		owpSum = 0
		played = 0
		for k in range(numTeams):
			if i == k:
				continue
			if data[i][k] == '.':
				continue
			played += 1
			team = data[k]
			#print team
			wins = 0
			losses = 0
			for j in range(numTeams):
				if j == i:
					continue
				if team[j] == '1':
					wins += 1
				elif team[j] == '0':
					losses += 1
			owpSum += wins/ float(wins + losses)
			#print " --- ", i, k, wins/float(wins + losses)
			#print " ---- ", wins, losses
		owp.append(owpSum / played)
		#print " - ", owpSum / (numTeams-1)
	
	oowp = []
	for i in range(numTeams):
		oowpSum = 0
		played = 0
		for j in range(numTeams):
			if i == j:
				continue
			if data[i][j] == '.':
				continue
			else:
				oowpSum += owp[j]
				played += 1
				#print "--", owp[j]
		#print oowpSum
		#print played, oowpSum / float(played)
		oowp.append(oowpSum / float(played))
	
	#print wp
	#print owp
	#print oowp
	
	print "Case #%s:" % (caseNum)
	
	rpi = []
	for i in range(numTeams):
		print 0.25*wp[i] + 0.50*owp[i] + 0.25*oowp[i]
	
	"""
	numVals = int(infile.readline())
	nums = [int(i) for i in infile.readline().split()]
	nums.sort()
	nums.reverse()
	
	totalXor = 0
	for i in nums:
		totalXor ^= i
		
	if totalXor != 0 or len(nums) < 2:
		print "Case #%s: NO" % (caseNum)
		continue
	else:
		print "Case #%s: %s" % (caseNum, sum(nums[:-1]))
	"""
