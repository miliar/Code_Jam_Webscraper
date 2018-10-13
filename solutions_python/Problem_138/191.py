file = open('input', 'r')

problems = int(file.readline())

for x in range(1, problems+1):
	points_regular = 0
	points_deceitful = 0
	ignore = file.readline() # not really interesting
	naomi = file.readline().split()
	ken = file.readline().split()
	for i in range(0, len(naomi)):
		naomi[i] = float(naomi[i])
		ken[i] = float(ken[i])
	naomi.sort()
	ken.sort()
	naomi2 = list(naomi)
	ken2 = list(ken)
	# regular game	
	for i in range(0, len(naomi)):
		naomi_plays = naomi.pop(0)
		j = 0
		while ken[j] < naomi_plays:
			j = j + 1
			if j >= len(ken):
				j = 0
				break
		if naomi_plays > ken[j]: 
			points_regular = points_regular + 1	
		ignore = ken.pop(j) # not really interesting
	# deceitful game
	naomi = naomi2
	ken = ken2
	for i in range(0, len(naomi)):
		if naomi[0] > ken[0]: # trick ken; he'll throw away his lowest card because he thinks he has no chance
			ignore = naomi.pop(0) # both play the lowest card
			ignore = ken.pop(0)
			points_deceitful = points_deceitful + 1	
		else:
			ignore = naomi.pop(0) # naomi plays the lowest card but tricks ken into playing his highest!
			ignore = ken.pop()
	print "Case #" + str(x) + ": " + str(points_deceitful) + " " +str(points_regular)
