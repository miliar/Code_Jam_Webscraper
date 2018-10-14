import numpy as np

f = open("./A-large.in")
f_out = open('out.txt','w')

num_trials = f.readline()

def process(line, T):
	line = [1 if x == "X" else x for x in line]
	line = [-1 if x == "O" else x for x in line]
	line = [0 if x == "." else x for x in line]
	line = [T if x == "T" else x for x in line]
	return line
	
def process(line, T):
	line = [1 if x == "X" else x for x in line]
	line = [-1 if x == "O" else x for x in line]
	line = [0 if x == "." else x for x in line]
	line = [T if x == "T" else x for x in line]
	return line

def didwin(board, winsum):
	if winsum in [sum(line) for line in board]:
		return True
	elif winsum in [sum(line) for line in np.rot90(board)]:
		return True
	elif board[0][0] + board[1][1] + board[2][2] + board[3][3] == winsum:
		return True
	elif board[3][0] + board[2][1] + board[1][2] + board[0][3] == winsum:
		return True
	else:
		return False
		
def emptyspots(board):
	howmanyzeros = sum([0 in line for line in board])
	#print howmanyzeros
	return howmanyzeros > 0

		
for i in range(int(num_trials)):

	rows = [list(f.readline().strip()), list(f.readline().strip()),list(f.readline().strip()),list(f.readline().strip())]

	arrayX = [process(row, 1) for row in rows]
	arrayO = [process(row, -1) for row in rows]
	if didwin(arrayX, 4) or didwin(arrayO, 4):
		f_out.write("Case #%d: X won\n" % (i + 1))
	elif didwin(arrayX, -4) or didwin(arrayO, -4):
		f_out.write("Case #%d: O won\n" % (i + 1))
	elif emptyspots(arrayX):
		f_out.write("Case #%d: Game has not completed\n" % (i + 1))
	else:
		f_out.write("Case #%d: Draw\n" % (i + 1))
	
	#print array
	#print np.rot90(array)
	
	f.readline()
	
f.close()
f_out.close()
