import os

def GetAverage(tokens, j):
	avg = 0
	for i in range(0, len(tokens)):
		avg = avg + tokens[i][j][1]
	return avg / len(tokens)

def GetClosestToAverage(tokens, j, avg):
	closest = tokens[0][j][1]
	for i in range(1, len(tokens)):
		if abs(closest - avg) > abs(tokens[i][j][1] - avg):
			closest = tokens[i][j][1]
	#print(closest)
	return closest

def GetMovesToClosest(tokens, j, closest):
	moves = 0
	for i in range(0, len(tokens)):
		moves += abs(tokens[i][j][1] - closest)
	return moves

def GetMoves(tokens):
	moves = 0
	for j in range(0, len(tokens[0])):
		avg = GetAverage(tokens, j)
		closest = GetClosestToAverage(tokens, j, avg)
		moves += GetMovesToClosest(tokens, j, closest) 
	return moves

def CheckPossible(tokens):
	if len(tokens) > 1:
		length = len(tokens[0])
		for i in range(1, len(tokens)):
			if length != len(tokens[i]):
				return False
		for j in range(0, len(tokens[0])):
			for i in range(1, len(tokens)):
				if tokens[i][j][0] != tokens[0][j][0]:
					return False
	return True

def Tokenise(strings):
	tokens = []
	for i in range(0, len(strings)):
		tokens.append([])
		char = strings[i][0]
		index = 0
		for j in range(0, len(strings[i])):
			if (strings[i][j] != char):
				tokens[i].append([char, j - index])
				char = strings[i][j]
				index = j
		tokens[i].append([char, j - index + 1])
	return tokens

t = int(input())
for ti in range(1, t + 1):
	n = int(input())
	strings = []
	for ni in range(0, n):
		strings.append(input().strip())
	tokens = Tokenise(strings)
	#print(tokens)
	if not CheckPossible(tokens):
		print("Case #" + str(ti) + ": Fegla Won")
	else:
		print("Case #" + str(ti) + ": " + str(GetMoves(tokens)))
