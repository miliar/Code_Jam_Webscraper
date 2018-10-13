import sys

def check_win(r):
	xrs = [i for i in r if i=="X" or i=="T" ]
	ors = [i for i in r if i=="O" or i=="T" ]
	if len(xrs)==4:
		return "X won"
	elif len(ors)==4:
			return "O won"
	else:
		return ""	
			
def check_finished(game):
	for r in game:
		for c in r:
			if c == ".":
				return "Game has not completed"
	return "Draw"

def solve(game):
	for r in game:
		win = check_win(r) 
		if win != "":
			return win
	for i in range(4):
		c = [r[i] for r in game]
		win = check_win(c) 
		if win != "":
			return win
	
	d1 = [game[i][i] for i in range(4)]
	win = check_win(d1) 
	if win != "":
		return win
	d2 = [game[i][3-i] for i in range(4)]
	win = check_win(d2) 
	if win != "":
		return win		
	return check_finished(game)

N = int(sys.stdin.readline().strip())

for t in range(N):
	game=[]
	for i in range(4):
		game.append(sys.stdin.readline().strip())
	if t<N:
		sys.stdin.readline().strip()		
	print "Case #{0}: {1}".format(t+1, solve(game))