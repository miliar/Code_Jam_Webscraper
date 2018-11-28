def nextPos(player,l):
	if (player ==1): #blue
		for i in xrange(0,len(l)*2,2):
			try:
				if l[i] == 'B':
					return int(l[i+1])
			except:
				return 0
	else:
		for i in xrange(0,len(l)*2,2):
			try:
				if l[i] == 'O':
					return int(l[i+1])
			except:
				return 0

for t in xrange(int(raw_input())):
	inline = raw_input().split()
	instructions = int(inline.pop(0))
	
	blueDest = 0
	oranDest = 0
	
	bluePos = 1
	oranPos = 1
	
	toMove = 1 #the player to move. 1 for B
	
	time = 0
	
	total = 0
	
	for i in xrange(0,instructions*2,2):
		if inline[i] == 'B':
			toMove = 1
		elif inline[i] == 'O':
			toMove = 2
			
		blueDest = nextPos(1,inline[i:])
		oranDest = nextPos(2,inline[i:])
		
		if toMove == 1:
			time = abs(blueDest-bluePos) + 1# for pushing the button
			total += time
			bluePos = blueDest #advance to where it must be and it presses the button
			
			if (oranPos != oranDest):
				if (abs(oranDest-oranPos) <= time):
					oranPos = oranDest
				else: #if it cannot get there in time
					oranPos = oranDest + (abs(oranDest-oranPos)) - time#advance as close as possible
		elif toMove ==2:
			time= abs(oranDest-oranPos) + 1
			total += time
			oranPos = oranDest
			
			if (bluePos != blueDest):
				if (abs(blueDest-bluePos) <= time):
					bluePos = blueDest
				else:
					bluePos = blueDest + (abs(blueDest-bluePos)) - time
					

	
	print 'Case #'+str(t+1)+': '+str(total)