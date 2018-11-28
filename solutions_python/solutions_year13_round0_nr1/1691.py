#!/urs/bin/env python3
world = []
win = 1

def test_game_over():
	for i in range(4):
		for j in range(4):
			if world[i][j] == '.':
				return 1
	return 0


def test():
	global world
	test_lines()


def test_rows(k):
	for j in range(4):
		win = 1
		for i in range(3):
			if world[i][j]=='T':
				x = i
				y = j
				world[i][j]=world[i+1][j]
			if world[i+1][j]=='T':
				x = i+1
				y = j
				world[i+1][j]=world[i][j]
			if (world[i][j] != world[i+1][j]) or (world[i][j]=='.'):
				win = 0
				break
		if win == 1:
			print('Case #{}: {} won'.format(k,world[i][j]))
			return 1
		else:
			try:
				world[x][y]='T'
			except:
				pass
	return 0


def test_lines(k):
	global win
	for i in range(4):
		win = 1
		for j in range(3):
			if world[i][j]=='T':
				x = i
				y = j
				world[i][j]=world[i][j+1]
			if world[i][j+1]=='T':
				x = i
				y = j+1
				world[i][j+1]=world[i][j]
			if (world[i][j] != world[i][j+1]) or (world[i][j]=='.'):
				win = 0
				break
		if win == 1:
			print('Case #{}: {} won'.format(k,world[i][j]))
			return 1 
		else:
			try:
				world[x][y]='T'
			except:
				pass
	return 0


def test_diagonal1(k):
	win = 1
	for i in range(3):
		if world[i][i]=='T':
			x = i
			world[i][i]=world[i+1][i+1]
		if world[i+1][i+1]=='T':
			x = i+1
			world[i+1][i+1]=world[i][i]
		if (world[i][i] != world[i+1][i+1]) or (world[i][i]=='.'):
			win = 0
			break
	if win == 1:
		print('Case #{}: {} won'.format(k,world[i][i]))
		return 1 
	else:
		try:
			world[x][x]='T'
		except:
			pass
	return 0


def test_diagonal2(k):
	win = 1
	for i in range(3):
		if world[i][3-i]=='T':
			x = i
			y = 3-i
			world[i][3-i]=world[i+1][3-i-1]
		if world[i+1][3-i-1]=='T':
			x = i+1
			y = 3-i-1
			world[i+1][3-i-1]=world[i][3-i]
		if (world[i][3-i] != world[i+1][3-i-1]) or (world[i][3-i]=='.'):
			win = 0
			break
	if win == 1:
		print('Case #{}: {} won'.format(k,world[i][3-i]))
		return 1 
	else:
		try:
			world[x][y]='T'
		except:
			pass
	return 0


with open ('input.txt') as input:
	test = int(input.readline())
	k = 1
	for line in input:
		if line == '\n':
			if test_rows(k) or test_lines(k) or test_diagonal1(k) or test_diagonal2(k):
				pass
			else:
				if(test_game_over()):
					print('Case #{}: Game has not completed'.format(k))
				else:
					print('Case #{}: Draw'.format(k))
			k += 1
			world = []
		else:
			world.append(list(line[:-1]))	