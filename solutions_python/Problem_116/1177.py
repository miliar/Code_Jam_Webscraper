import sys

def checkLine(board, line):
				#print line
				#print [board[x[0]][x[1]] for x in line]
				counts = {'X':0,'O':0,'.':0,'T':0}
				for position in line:
								counts[board[position[0]][position[1]]] += 1

				necessary = 4
				if (counts['T'] == 1):
								necessary = 3

				ret = 'F'
				if (counts['X'] == necessary):
								ret = 'X'
				elif (counts['O'] == necessary):
								ret = 'O'
				elif (counts['.'] > 0):
								ret = '.'
				#print ret
				return ret

def checkBoard(board):
				haveEmpty = False
				idxs = range(4)
				linesToCheck = []
				#print board
				for i in range(4):
								row = [(i,x) for x in idxs]
								linesToCheck.append(row)
								column = [(x,i) for x in idxs]
								linesToCheck.append(column)
				linesToCheck.append([(x,x) for x in idxs])
				linesToCheck.append([(x,3-x) for x in idxs])

				for line in linesToCheck:
								result = checkLine(board, line)
								if (result == 'X' or result == 'O'):
												return result
								elif result == '.':
												haveEmpty = True
				if haveEmpty:
								return '.'
				return 'F'


lines = [x.strip() for x in open(sys.argv[1]).readlines()]
numCases = int(lines[0])
lines = lines[1:]
outcomes = {'X':'X won', 'O':'O won', 'F':'Draw', '.':'Game has not completed'}
for i in range(numCases)[:]:
				boardLines = lines[i*5:i*5+4]
				board = boardLines #[x.split('') for x in boardLines]
				result = checkBoard(board)
				print "Case #%d: %s" % ((i+1), outcomes[result])
				
