'''
Created on 2013-04-13

@author: ashwin
'''

from itertools import izip

def check(board):
	
	done = True
	for row in board:
		xcount, ocount = 0, 0
		for c in row:
			if c == "X" or c=="T":
				xcount += 1
			if c == "O" or c=="T":
				ocount += 1
			if c == '.':
				done = False
		
		if xcount == 4:
			return "X won"
		if ocount == 4:
			return "O won"
		
	for col in izip(*board):
		xcount, ocount = 0, 0
		for c in col:
			if c == "X" or c=="T":
				xcount += 1
			if c == "O" or c=="T":
				ocount += 1
			if c == '.':
				done = False
	
		if xcount == 4:
			return "X won"
		if ocount == 4:
			return "O won"
	
	xcount, ocount = 0, 0
	for i in xrange(4):
		if board[i][i] == "X" or board[i][i] == "T":
			xcount += 1
		if board[i][i] == "O" or board[i][i] == "T":
			ocount += 1
		
	if xcount == 4:
		return "X won"
	if ocount == 4:
		return "O won"
		
	xcount, ocount = 0, 0
	for i in xrange(4):
		if board[i][-1-i] == "X" or board[i][-1-i] == "T":
			xcount += 1
		if board[i][-1-i] == "O" or board[i][-1-i] == "T":
			ocount += 1
		
	if xcount == 4:
		return "X won"
	if ocount == 4:
		return "O won"
		
	
	if not done:
		return "Game has not completed"
	return "Draw"
	
def run(infilepath, outfilepath):
	with open(infilepath) as infile, open(outfilepath, 'w') as outfile:
		T = int(infile.readline().strip())
		for case in xrange(1,T+1):
			board = [infile.readline().strip() for _ in xrange(4)]
			infile.readline()
			status = check(board)
			outfile.write("Case #%d: %s\n" %(case, status))

if __name__ == "__main__":
	print 'starting'
	run('/Users/ashwin/Desktop/A-large.in', '/Users/ashwin/Desktop/testout.txt')
	print 'done'