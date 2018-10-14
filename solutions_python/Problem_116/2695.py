import sys

file = open("A-small-attempt2.in")

inputs = []

while 1:
    line = file.readline()
    if not line:
        break
    inputs.append(line)

for i in xrange(len(inputs)-1):
	inputs[i] = inputs[i][:-1]


num_games = int(inputs[0])

# 0 is game not finished
# 1 is draw
# 2 is X
# 3 is O
def check_four(a,b,c,d):
	if a == '.':
		return 0
	if a != 'T':
		if (a != b) and (b != 'T'):
			return 1
		elif b != c  and (c != 'T'):
			return 1
		elif c != d  and (d != 'T'):
			return 1
		elif (a == 'X'):
			return 2
		else:
			return 3
	else:
		if b != c:
			return 1
		elif c != d:
			return 1
		elif (b == 'X'):
			return 2
		else:
			return 3	

def check_game(game):
	empty_spaces = False
	for i in range(4):
		res = check_four(game[i][0],game[i][1],game[i][2],game[i][3])
		if res == 2:
			return 2
		elif res == 3:
			return 3
		elif res == 0:
			empty_spaces = True
	for i in range(4):
		res = check_four(game[0][i],game[1][i],game[2][i],game[3][i])
		if res == 2:
			return 2
		elif res == 3:
			return 3
		elif res == 0:
			empty_spaces = True
	res = check_four(game[0][0],game[1][1],game[2][2],game[3][3])
	if res == 2:
		return 2
	elif res == 3:
		return 3
	elif res == 0:
		empty_spaces = True
	res = check_four(game[0][3],game[1][2],game[2][1],game[3][0])
	if res == 2:
		return 2
	elif res == 3:
		return 3
	elif res == 0:
		empty_spaces = True
	if empty_spaces:
		return 0
	else:
		return 1

# game = inputs[26:30]
# print game

for i in xrange(num_games):
	res = check_game(inputs[(5*i)+1:(5*i)+5])
	if res == 0:
		tex = "Game has not completed"
	elif res == 1:
		tex = "Draw"
	elif res == 2:
		tex = "X won"
	else:
		tex = "O won"
	print "Case #"+str(i+1)+": "+tex


