#! /usr/bin/env python
import copy

isPossible = False
boardResult = ''
def calNumber(board, rCount, cCount):
	for r in range(rCount):
		for c in range(cCount):
			totalMine = 0
			if board[r][c] == '.':
				temp = list()
				if 0 < r < rCount-1:
					temp.append(board[r-1][c-1 if c >0 else 0 : c + 2 if c < cCount else cCount])
					temp.append(board[r][c-1 if c >0 else 0 : c + 2 if c < cCount else cCount])
					temp.append(board[r+1][c-1 if c >0 else 0 : c + 2 if c < cCount else cCount])
				elif r == 0:
					temp.append(board[r][c-1 if c >0 else 0 : c + 2 if c < cCount else cCount])
					temp.append(board[r+1][c-1 if c >0 else 0 : c + 2 if c < cCount else cCount])
				elif r == rCount - 1:
					temp.append(board[r-1][c-1 if c >0 else 0 : c + 2 if c < cCount else cCount])
					temp.append(board[r][c-1 if c >0 else 0 : c + 2 if c < cCount else cCount])
				totalMine += countMine(temp)
				board[r][c] = str(totalMine)

def countMine(part):
	totalMine = 0;
	for r in part:
		for c in r:
			if c == '*':
				totalMine += 1
	return totalMine

def addZero(board, rCount, cCount, r, c, mCount):
	global isPossible, boardResult
	board[r][c] = '0'
	formBoard(board, rCount, cCount)
	calNumber(board, rCount, cCount)
	if countMine(board) == mCount:
		isPossible = True
		for x in range(0, rCount):
			flag = False
			for y in range(0,cCount):
				if board[x][y] == '0' :
					board[x][y] ='c'
					flag = True
					break
			if flag:
				break
		for x in board:
			for y in x:
				if y == 'c' or y == '*':
					boardResult += y
				else:
					boardResult += '.'
			boardResult += '\n'
		return
	if countMine(board) < mCount:
		return
	for r in range(rCount):
		for c in range(cCount):
			if board[r][c] == '0':
				rStart = r-1 if r > 0 else 0
				rEnd = r+2 if r < rCount-1 else rCount
				cStart = c-1 if c >0 else 0
				cEnd = c + 2 if c < cCount-1 else cCount
				for i in range(rStart, rEnd):
					for j in range(cStart, cEnd):
						if board[i][j] != '0' and board[i][j] != '-1':
							temp = copy.deepcopy(board)
							addZero(temp, rCount, cCount, i, j, mCount)
							if isPossible:
								return
							board[i][j] = '-1'
def formBoard(board, rCount, cCount):
	for r in range(rCount):
		for c in range(cCount):
			if board[r][c] == '0':
				rStart = r-1 if r > 0 else 0
				rEnd = r+2 if r < rCount-1 else rCount
				cStart = c-1 if c >0 else 0
				cEnd = c + 2 if c < cCount-1 else cCount
				for i in range(rStart, rEnd):
					for j in range(cStart, cEnd):
						if board[i][j] != '0':
							board[i][j] = '.'

inFile = open("C-small-attempt4.in.txt", 'r')
lineCounter = int(inFile.readline())
co = 1
results = ""
while co <= lineCounter:
	isPossible = False
	infos = inFile.readline();
	infoList = infos.split(' ')
	rCount = int(infoList[0])
	cCount = int(infoList[1])
	mCount = int(infoList[2])
	boardResult = ''
	if rCount == 1 or cCount == 1:
		isPossible = True
		if rCount == 1:
			boardResult += 'c'
			for i in range(cCount - mCount - 1):
				boardResult += '.'
			for i in range(mCount):
				boardResult += '*'
			boardResult += '\n'
		elif cCount == 1:
			boardResult += 'c\n' 
			for i in range(rCount - mCount -1):
				boardResult += '.\n'
			for i in range(mCount):
				boardResult += '*\n'
	elif rCount == 2 or cCount == 2:
		if (mCount%2 != 0 or rCount*cCount - mCount < 4) and rCount*cCount - mCount != 1:
			isPossible = False
		elif rCount*cCount - mCount == 1:
			isPossible = True
			if rCount == 2:
				for i in range(2):
					if i == 0:
						boardResult += 'c' + '*'*(cCount - 1) + '\n'
					else:
						boardResult += '*' * cCount + '\n'
			elif cCount == 2:
				for i in range(rCount):
					if i == 0:
						boardResult += 'c*\n'
					else:
						boardResult += '**\n'
		elif rCount == 2:
			isPossible = True
			for i in range(2):
				if i == 0:
					boardResult += 'c' + '.' *(cCount - mCount/2 -1) + '*' * (mCount/2) + '\n'
				else:
					boardResult += '.' * (cCount - mCount/2) + '*' * (mCount/2) + '\n'
		elif cCount == 2:
			isPossible = True
			for i in range(rCount):
				if i == 0:
					boardResult += 'c.\n'
				elif i < rCount - mCount/2:
					boardResult += '..\n'
				else:
					boardResult += '**\n'
	else:
		board = list()
		#init the board
		for r in range(rCount):
			t = list()
			for c in range(cCount):
				t.append('*')
			board.append(t)
		if rCount*cCount - mCount ==  1:
			isPossible = True
			for r in range(rCount):
				if r == 0:
					boardResult += 'c' + '*'*(cCount-1) + '\n'
				else:
					boardResult += '*' * cCount + '\n'
		addZero(board, rCount, cCount, 0, 0, mCount)
	if isPossible:
		results += "Case #" + str(co) + ": " + "\n"+ boardResult
	else:
		results += "Case #" + str(co) + ": " + "\n" +"Impossible" + '\n'
	co += 1
outFile = open("C-small.txt", 'w')
outFile.write(results[0:len(results)-1])