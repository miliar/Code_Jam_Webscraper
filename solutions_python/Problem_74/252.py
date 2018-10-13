from collections import deque
f = open('botinput.txt','r')

trials = int(f.readline())
orange = 'O'
blue = 'B'

for i in xrange(1,trials+1):
	ordered_moves = deque([])
	bots = {orange: deque([]), blue: deque([])}
	position = {orange: 1, blue: 1}
	info = f.readline().split()
	num_presses = int(info[0])
	for j in range(1,len(info),2):
		bot = info[j]
		button_press = int(info[j+1])
		ordered_moves.append((bot,button_press))
		bots[bot].append(button_press)
		#print "Bot {0} presses button {1}".format(bot,button_press)
	time = 0
	while len(ordered_moves) > 0:
		bot, move = ordered_moves[0]
		ordering = []
		if(bot == blue):
			ordering = [orange,blue]
		else:
			ordering = [blue,orange]
		
		#print "Move %d"%(time+1)
		#print "Waiting for '{0}' to press button at {1}".format(bot,move)
		for robot in ordering:
			if(len(bots[robot]) > 0):
					if(bot == robot and position[robot] == move):
						#print "%s has pressed button at %d"%(robot,position[robot])
						bots[robot].popleft()
						ordered_moves.popleft()
					else:
						desired = bots[robot][0]
						if(desired > position[robot]):
							#print "%s is moving from %d to %d towards %d" % (robot,position[robot], position[robot]+1 ,desired)
							position[robot] += 1
						elif (desired < position[robot]):
							#print "%s is moving from %d to %d towards %d" % (robot,position[robot], position[robot]-1,desired)
							position[robot] -= 1
						else:
							#print "%s is waiting" % robot
							continue
			else:
				#print "%s is done" % robot
				continue
		time +=1
	print "Case #{0}: {1}".format(i,time)
	#print "\n\n"