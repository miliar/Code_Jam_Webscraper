f = open('A-large.in','r')
prompt = f.readlines()
f.close()
prompt = ''.join(prompt)



def check(player,tile):
	if tile == player or tile == 'T':
		return True
	return False

def win(p,b):
	#b looks like this
	#
	#	0	1	2	3
	#	4	5	6	7
	#	8	9	10	11
	#	12	13	14	15
	#

	#winning conditions
	#vertical
	#	0<=x<4 and x and x+4 and x+8 and x+12
	#horizantal
	#	x%4 == 0 and x and x+1 and x+2 and x+3
	#diagonals
	#	(0 and 5 and 10 and 15) or (3 and 6 and 9 and 12)
	if check(p,b[0]) and check(p,b[5]) and check(p,b[10]) and check(p,b[15]):
		return True
	if check(p,b[3]) and check(p,b[6]) and check(p,b[9]) and check(p,b[12]):
		return True
	for a in xrange(0,4):
		if check(p,b[a]) and check(p,b[a+4]) and check(p,b[a+8]) and check(p,b[a+12]):
			return True
		y = a*4
		if check(p,b[y]) and check(p,b[y+1]) and check(p,b[y+2]) and check(p,b[y+3]):
			return True

def who_won(board):
	if win('X',board):
		return 'X'
	if win('O',board):
		return 'O'
	if '.' not in board:
		return 'D'
	return 'I'





num  = prompt.split('\n',1)[0]
sets = prompt.split('\n',1)[1]
count = 0
final_string = ''
for a in sets.split("\n\n"):
	count += 1
	if count > int(num):
		break
	if a[-1] == "\n":
		a = a[:-1]
	a = a.replace('\n','')
	winner = who_won(a)
	s = 'Case #' + str(count) + ": "
	if winner == 'X':
		s += "X won"
	elif winner == 'O':
		s += "O won"
	elif winner == 'D':
		s += "Draw"
	elif winner == 'I':
		s += "Game has not completed"
	final_string += s + "\n"
f = open('output1long.txt','w')
f.write(final_string)
f.close()