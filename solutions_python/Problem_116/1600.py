
def match(string):
	matched = True
	c1 = string[0]
	if c1 == " " or c1 == ".":
		return False
	for char in string:
		if char != c1 and char != "T":
			matched = False
	if(matched):
		return c1
	else:
		return False

def check_game_hor(game):
	for line in game:
		if match(line):
			return match(line)
	return False

def check_game_vert(game):
	for i in range(len(game)):
			if match(game[0][i]+game[1][i]+game[2][i]+game[3][i]): return match(game[0][i]+game[1][i]+game[2][i]+game[3][i])
	return False

def check_game_diag(game):
	if match(game[0][0]+game[1][1]+game[2][2]+game[3][3]): return match(game[0][0]+game[1][1]+game[2][2]+game[3][3])
	if match(game[0][3]+game[1][2]+game[2][1]+game[3][0]): return match(game[0][3]+game[1][2]+game[2][1]+game[3][0])
	return False

def check_game_stale(game):
	for line in game:
		for i in range(len(line)):
			if line[i] == ".":
				return False
	return True

lines = []
for line in file("q1inp.txt"):
	lines.append(line)

num = int(lines[0])
print num

offset = 1
for i in range(num):
	game = []
	for ii in range(4):
		game.insert(ii, lines[ii+offset].strip())

	offset += 5
	print ("Case #%d" % i+1),
	#print game
	if check_game_hor(game):
		print check_game_hor(game), " won"
		continue
	if check_game_vert(game):
		print check_game_vert(game), " won"
		continue
	if check_game_diag(game):
		print check_game_diag(game), " won"
		continue
	if check_game_stale(game):
		print "Draw"
		continue
	print "Game has not completed"

