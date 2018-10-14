T = int(raw_input())

def solveCase(N,seq):
	playersPos = [1,1]
	lastT = [0,0]
	index = None
	lastMovePlayer = None
	secs = 0
	for n in range(N) :
		index = int(seq[n*2+1])
		player = seq[n*2]
		if player == 'O':
			player = 0
		else :
			player = 1
		
		move = abs(index-playersPos[player])
		if lastMovePlayer != player :
			timeNeededForMove = move - abs(lastT[0]-lastT[1])
		else:
			timeNeededForMove = move
		
		if (timeNeededForMove < 0) :
			timeNeededForMove = 0
		playersPos[player] = index
		lastT[player] = max(lastT)+timeNeededForMove+1
		lastMovePlayer = player
		
		#print "Player %d index %d" % (player,index)
		#print "Move of %d" %(move)
		#print "Time needed for the move %d " % (timeNeededForMove)
		#print "Time for current order : %s" % (lastT)
	return max(lastT)
		
for t in range(1,T+1):
	l = raw_input().split()
	seq = l[1:]
	N = int(l[0])
	
	
	y = solveCase(N,seq)
	print "Case #%d: %d" % (t,y)