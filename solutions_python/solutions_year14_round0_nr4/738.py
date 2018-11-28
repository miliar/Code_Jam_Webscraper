
T = int(raw_input())
for t in xrange(T) :
	N = int(raw_input())
	#print N
	Naomi = map(float,raw_input().split())
	Ken = map(float,raw_input().split())
	
        #print Naomi
	#print Ken

        text = "Case #"+str(t+1)+": "
 	
	Ken_org = Ken[:]
	Naomi_org = Naomi[:]
 	
	score = 0
	for Nblock in Naomi :
		Kblocks = [b for b in Ken if b>Nblock]
		if len(Kblocks) == 0 :
			#Naomi wins round
			Krem = min(Ken)
			score+=1
		else :
			#Ken wins round
			Krem = min(Kblocks)
		#print Nblock, Krem
		Ken.remove(Krem)
		#print Ken
	#print "score = ", score

	Ken = Ken_org[:]
	#print Ken, Naomi
	dscore = 0
	Naomi = sorted(Naomi)[::-1]
	for Nblock in Naomi :
		Kblocks = [b for b in Ken if b<Nblock]
		if len(Kblocks) == 0 :
			#Ken wins round
			Krem = min(Ken)
		else :
			#Naomi wins round
			Krem = max(Kblocks)
			dscore+=1
		#print Nblock, Krem
		Ken.remove(Krem)
		#print Ken
	#print "dscore = ", dscore
	print text+str(dscore) + " " + str(score)

