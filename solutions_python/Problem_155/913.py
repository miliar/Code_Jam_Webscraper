T=int(raw_input())
for i in range(T):
	line=raw_input().split()
	sMax=int(line[0])
	sVect=line[1]
	friendsNeeded=0
	sum=0
	for j in range(sMax):
		sum+=int(sVect[j])
		if sum+friendsNeeded<j+1:
			friendsNeeded+=j+1-sum-friendsNeeded
	print "Case #"+str(i+1)+": "+str(friendsNeeded)
