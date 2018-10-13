# Solution to "Tic-Tac-Toe-Tomek" for Google Code Jam 2013
# by Peter Mattsson (quantum.caffeine@gmail.com)
import sys
import string

with open(sys.argv[1], 'r') as f:
	numCases = int(f.readline())
	cases = []
	for c in range(numCases):
		cases.append(tuple(f.readline()[:4] for _ in range(4)))
		if c < numCases-1:
			f.readline()
f = open(sys.argv[2], 'w')

def lines(board):
	for row in board:
		yield row
	for col in [''.join(row[c] for row in board) for c in range(4)]:
		yield col
	yield ''.join(board[a][a] for a in range(4))
	yield ''.join(board[a][3-a] for a in range(4))

for c,case in enumerate(cases):
	done = False
	for line in lines(case):
		if ('.' in line) or (('X' in line) and ('O' in line)): continue
		if 'X' in line:
			f.write("Case #%d: %s\n"%(c+1, "X won"))
		elif 'O' in line:
			f.write("Case #%d: %s\n"%(c+1, "O won"))
		done = True
		break
	if not done:
		if '.' in ''.join(line for line in case):
			f.write("Case #%d: %s\n"%(c+1, "Game has not completed"))
		else:
			f.write("Case #%d: %s\n"%(c+1, "Draw"))

f.close()