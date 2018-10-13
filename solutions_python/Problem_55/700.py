#!/usr/bin/python

f = open('C-small-attempt0.in','r')
w = open('output.txt','w')
testCases = f.readline()
nTestCases = int(testCases)

for i in range(nTestCases):
	rkn = [int(s) for s in f.readline().split(' ')]
	g = [int(s) for s in f.readline().split(' ')]
	nRuns = rkn[0]
	coasterSize = rkn[1]
	nGroups = rkn[2]
	
	money = 0
	
	# Handles the special situation where total # of ppl in line < coasterSize
	if sum(g) < coasterSize:
		money = nRuns * sum(g)
	else:
		groupNumber = 0
		for j in range(nRuns):
			nPeopleInCoaster = 0
			while nPeopleInCoaster + g[groupNumber] <= coasterSize:
				nPeopleInCoaster = nPeopleInCoaster + g[groupNumber]
				groupNumber = (groupNumber + 1) % nGroups
			money = money + nPeopleInCoaster
	
	w.write('Case #{0}: {1}\n'.format(i+1,money) )
