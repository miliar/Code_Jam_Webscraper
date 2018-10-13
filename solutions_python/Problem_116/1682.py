import sys
import numpy as np


f = open('A-large.txt','w')
stdin = open('A-large.in', 'r')
T = int(stdin.next().strip())
for t in xrange(1,T+1):
	board = np.array([list(stdin.next().strip()) for i in xrange(4)])
	stdin.next().strip()
	
	check = []
	for i in range(4):
		check.append(''.join(board[:,i].tolist()))
		check.append(''.join(board[i].tolist()))
	check.append(''.join(board.diagonal().tolist()))
	check.append(''.join([board[0][3],board[1][2],board[2][1],board[3][0]]))	
	
	winner = 'Game has not completed'
	empty_space = False
	
	if '.' in ''.join(board.flatten().tolist()): 
		empty_space = True
	
	for c in check:
		if not '.' in c:
				if not 'O' in c:
					winner = 'X won'
					break
				elif not 'X' in c:
					winner = 'O won'
					break		
		
	if winner == 'Game has not completed' and empty_space == False:
		winner = 'Draw'	
		
			
	#print 'Case #%d: %s' % (t, winner)
	
	f.write("""Case #"""), f.write(str(t)), f.write(": "), f.write(str(winner)), f.write("\n")

f.close()	
	
	
	