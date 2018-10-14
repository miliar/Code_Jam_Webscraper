#!/usr/bin/python
import sys

input = sys.argv[1]
#output = sys.argv[2]

input = open(input).read().strip().split("\n")

cases = int(input[0].strip())
input = input[1:]

result = ""
index = 0
for i in range(0,cases):
	teamsNum = int(input[i+index])
	teams = {}
	for j in range(0,teamsNum):
		teams[j] = {}
		teams[j]["opps"] = []
	for j in range(i+index+1,i+index+1+teamsNum):
		games = input[j]
		gamesNum = 0
		gamesWon = 0.0
		opps = 0
		ci = 0
		for c in games:
			if c == "1":
				gamesNum += 1
				gamesWon += 1
				teams[j-(i+index+1)]["opps"].append(ci)
			elif c == "0":
				gamesNum += 1
				teams[j-(i+index+1)]["opps"].append(ci)
			elif c ==".":
				pass
			ci += 1
		teams[j-(i+index+1)]["wp"] = gamesWon / gamesNum
	for j in range(i+index+1,i+index+1+teamsNum):
		games = input[j]
		teams[j-(i+index+1)]["owp"] = {}
		for k in range(0,teamsNum):
			if k != j-(i+index+1):
				gamesNum = 0
				gamesWon = 0.0
				for u in range(0,teamsNum):
					if k != u and u != j-(i+index+1):
						c = games[u]
						if c == "1":
							gamesNum += 1
							gamesWon += 1
						elif c == "0":
							gamesNum += 1
						elif c ==".":
							pass
				if gamesWon == 0.0:
					teams[j-(i+index+1)]["owp"][k] = 0.0
				else:
					teams[j-(i+index+1)]["owp"][k] = gamesWon / gamesNum
	for k in range(0,teamsNum):
		owp = 0.0
		for u in range(0,teamsNum):
			if u != k and u in teams[k]["opps"]:
				owp += teams[u]["owp"][k]
		owp = owp / (len(teams[k]["opps"]))
		teams[k]["_owp"]  = owp
	for k in range(0,teamsNum):
		oowp = 0.0
		for u in range(0,teamsNum):
			if u != k and u in teams[k]["opps"]:
				oowp += teams[u]["_owp"]
		oowp = oowp / (len(teams[k]["opps"]))
		teams[k]["oowp"]  = oowp
	print "Case #"+str(i+1)+":"
	for k in range(0,teamsNum):
		print 0.25 * teams[k]["wp"] + 0.50 * teams[k]["_owp"] + 0.25 * teams[k]["oowp"]
	

	index += teamsNum
	
	
	
