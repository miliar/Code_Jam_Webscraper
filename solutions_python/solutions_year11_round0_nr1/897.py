f1 = open('a-large.in', 'r')
f2 = open('a-large.out', 'w')

cases = int(f1.readline().strip('\n'))

for c in xrange(1, cases + 1):
	
	inputlist = f1.readline().strip('\n').split()
	steps = int(inputlist[0])
	del inputlist[0]
	for step in xrange(0, steps * 2, 2):
		if inputlist[step] == 'O':
			inputlist[step] = 0
		else:
			inputlist[step] = -1
		inputlist[step + 1] = int(inputlist[step + 1])
	
	moves = []
	pos = [1, 1] # O, B
	for step in xrange(0, steps * 2, 2):
                curturn = inputlist[step]
                curmove = inputlist[step + 1]
                notturn = -1 - curturn
		reservedmove = inputlist[inputlist.index(notturn, step) + 1] if notturn in inputlist[step:steps * 2] else -1
		while True:
			nextmove = [0, 0]
			nextmove[notturn] = 0 if (reservedmove < 0 or reservedmove == pos[notturn]) else (1 if reservedmove > pos[notturn] else -1)
			pos[notturn] += nextmove[notturn]
			if curmove == pos[curturn]:
				nextmove[curturn] = 2
				moves.append(nextmove)
				break
			elif curmove > pos[curturn]:
				nextmove[curturn] = 1
				pos[curturn] += 1
			else:
				nextmove[curturn] = -1
				pos[curturn] -= 1
			moves.append(nextmove)
	
	f2.write('Case #' + str(c) + ': ' + str(len(moves)) + '\n')	

f1.close()
f2.close()
