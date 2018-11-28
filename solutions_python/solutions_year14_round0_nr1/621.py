import os

def ReadBoard():
	board = []
	for i in range(0, 4):
		line = input().split()
		board.append([])
		board[i].append(line[0])
		board[i].append(line[1])
		board[i].append(line[2])
		board[i].append(line[3])
	return board

def Solve(answer1, board1, answer2, board2):
	cards = []
	for i in range(0, 4):
		for j in range(0, 4):
			if board1[answer1][i] == board2[answer2][j] \
				and board1[answer1][i] not in cards:
				cards.append(board1[answer1][i])
	#print(str(answer1) + " " + str(answer2))			
	#print(cards)
	return cards


t = int(input())
for ti in range(1, t+1):
	answer1 = int(input()) - 1
	board1 = ReadBoard()
	answer2 = int(input()) - 1
	board2 = ReadBoard()
	cards = Solve(answer1, board1, answer2, board2)
	if len(cards) == 1:
		print("Case #" + str(ti) + ": " + str(cards[0]))
	elif len(cards) > 1:
		print("Case #" + str(ti) + ": Bad magician!")
	else:
		print("Case #" + str(ti) + ": Volunteer cheated!")