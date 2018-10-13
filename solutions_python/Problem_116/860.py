import math


def replace(c):
	if c == 'X':
		return 1
	if c == 'O':
		return 0
	if c == 'T':
		return 0.5
	return 10

def judge_line(list):
	if math.ceil(sum(list)) == 4:
		return 1
	elif math.floor(sum(list)) == 0:
		return 0
	return 2

def judge_case(i, lines):
	game = {}
	#Horizontal
	for j in range(0,4):
		game[j] =map(replace, list(lines[5*i + j + 1].split()[0]))
		test_h = judge_line(game[j])
		if test_h < 2:
			return test_h
	#Vertical
	for j in range(0,4):
		column = [game[l][j] for l in game]
		test_v = judge_line(column);
		if test_v < 2:
			return test_v
	#Diagnol
	test_d = judge_line([game[0][0], game[1][1], game[2][2], game[3][3]])
	if test_d < 2:
		return test_d
	test_d2 = judge_line([game[0][3], game[1][2], game[2][1], game[3][0]]) 
	if test_d2<2:
		return test_d2

	sum_lines = [sum(game[l]) for l in game]
	for sum_line in sum_lines:
		if sum_line >= 10:
			return 3

	return 4


def judge_all(filename):
	f = open(filename)
	lines = f.readlines()
	f.close

	num = int(lines[0])	
	for i in range(0, num):
		result = judge_case(i, lines)
		if result == 1:
			phrase = "X won"
		elif result == 0:
			phrase = "O won"
		elif result == 3:
			phrase = "Game has not completed"
		elif result == 4:
			phrase = "Draw"
		print "Case #" + str(i+1) + ": " + phrase

judge_all("A-large.in")










# print replace('O')