'''
Created on 13/04/2013

@author: shb
'''
import sys

def read_board():
	lines=[]
	for i in range(4):
		lines.extend(sys.stdin.readline().strip())
	sys.stdin.readline()
	return lines
def check_winner(board):
	lines = []
	for i in range(4):
		line = board[4*i:4*i+4]
		lines.append(line)

	for i in range(4):
		line = board[i::4]
		lines.append(line)
	
	lines.append(board[0::5])
	lines.append(board[3:13:3])

	
	for player in ('X', 'O'):
		for line in lines:
			if all([c==player or c=='T' for c in line]):
				return player
	return None


if __name__ == '__main__':
	n = int(sys.stdin.readline())
	for i in range(n):
		board = read_board()
		winner = check_winner(board)
		if winner is not None:
			print 'Case #{}: {} won'.format(i+1, winner)
		else:
			if any([c=='.' for c in board]):
				print 'Case #{}: Game has not completed'.format(i+1)
			else:
				print 'Case #{}: Draw'.format(i+1)