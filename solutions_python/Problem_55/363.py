f = file("C-large.in", "r")
of = file("C-large.out", "w")
lines = f.readlines()

cases = int(lines[0])
for i in range(cases):
	input1 = lines[i * 2 + 1].split(" ");
	r = int(input1[0])
	k = int(input1[1])
	n = int(input1[2])
	input2 = lines[i * 2 + 2].split(" ");
	groups = []
	for g in input2:
		groups.append(int(g))
	print "R=", r, "k=", k, "N=", n, "groups:", groups
	
	counts = []
	for j in groups:
		counts.append(None)
		
	runs = 0
	earnings = 0
	nextGroup = 0
	while runs < r and counts[nextGroup] == None:
		# mark current runs and earnings
		counts[nextGroup] = (runs, earnings)
		
		# take in as many groups as can fit
		spaceRemain = k
		groupsOnRide = 0
		while groupsOnRide < len(groups) and groups[nextGroup] <= spaceRemain:
			groupsOnRide += 1
			earnings += groups[nextGroup]
			spaceRemain -= groups[nextGroup]
			nextGroup += 1
			if nextGroup >= len(groups):
				nextGroup = 0

		runs += 1

	print "first runs:", runs, "earning:", earnings
		
	if counts[nextGroup]:
		periodLength = runs - counts[nextGroup][0]
		periodEarnings = earnings - counts[nextGroup][1]
		
		print "found period of", periodLength, "earnings", periodEarnings
	
		runsRemain = r - runs
		
		fullPeriods = int(runsRemain / periodLength)
		print "full periods:", fullPeriods, "added earnings:", fullPeriods * periodEarnings
		
		runs += fullPeriods * periodLength
		earnings += fullPeriods * periodEarnings
		
		print "runs after all full periods:", runs, "earnings:", earnings
		
		# add the remaining runs
		while runs < r:
			# take in as many groups as can fit
			spaceRemain = k
			groupsOnRide = 0
			while groupsOnRide < len(groups) and groups[nextGroup] <= spaceRemain:
				groupsOnRide += 1
				earnings += groups[nextGroup]
				spaceRemain -= groups[nextGroup]
				nextGroup += 1
				if nextGroup >= len(groups):
					nextGroup = 0
	
			runs += 1
			
		print "final runs:", runs, "earnings:", earnings

	else:
		print "completed day runs:", runs, "earnings:", earnings
	
	of.write("Case #%i: %i\n" % (i + 1, earnings))