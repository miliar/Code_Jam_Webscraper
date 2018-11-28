def inFile(path):
	fileHandle = open(path)
	fileList = fileHandle.readlines()
	fileHandle.close()
	
	DataSet = []
	comma = '\n'

	del fileList[0]
	while len(fileList) != 0:
		rawdata = fileList[0:4]
		data = dataHandle(rawdata)
		DataSet.append(data)
		del fileList[0:4+1]

	return DataSet

def dataHandle(data):
	board = []  #one round board display
	for d in data:
		row = d.strip('\n')
		board.append(row)
	return board

def outFile(path, resultset):
	fileHandle = open(path, 'w+')
	num = 1
	for data in resultset:
		t = 'Case #' + str(num) + ': ' + data + '\n'
		fileHandle.writelines(t)
		num += 1
	fileHandle.close

def position(board):
	x = []
	o = []
	blank = 0
	for i in range(0,4):
		for j in range(0,4):
			symbol = board[i][j]
			position = (i,j)
			if   symbol == 'X':
				x.append(position)
			elif symbol == 'O':
				o.append(position)
			elif symbol == 'T':
				x.append(position)
				o.append(position)
			elif symbol == '.':
				blank += 1
	return x, o, blank

def judge(x, o, blank):

	if IsWin(x) == True:
		return "X won"
	elif IsWin(o) == True:
		return "O won"
	elif blank == 0:
		return "Draw"
	else:
		return "Game has not completed"

def IsWin(symbol):
	IsWin = False
	c1 = 0
	c2 = 0
	for temp in symbol:
		if temp[0] == temp[1]:
			c1 += 1
		if temp[0]+temp[1] == 3:
			c2 += 1
	if c1 == 4 or c2 == 4:
		IsWin = True
		return IsWin
	for i in range(0,4):
		c3 = 0
		c4 = 0
		for temp in symbol:
			if temp[0] == i:
				c3 += 1
			if temp[1] == i:
				c4 += 1
		if c3 == 4 or c4 == 4:
			IsWin = True
			return IsWin	
	return IsWin

def game(dataset):
	results = []
	for board in dataset:
		x, o, blank = position(board)
		result = judge(x, o, blank)
		results.append(result)
	return results

if __name__ == '__main__':
	inpath = '/Users/inzen/in'
	outpath = '/Users/inzen/out'
	
	dataset = inFile(inpath)
	print dataset
	results = game(dataset)

	outFile(outpath, results)
