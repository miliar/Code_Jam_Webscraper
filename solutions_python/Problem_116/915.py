# -*- coding: utf-8 -*-

import io

def check_result(sum):
	""" sum of a row, a col or a diagonal, return 0 for no win, 1 for X win, -1 for O win """
	if sum < 100 and sum % 5 == 0:
		return 1
	elif sum < 100 and sum % 7 == 0:
		return -1
	else:
		return 0

def main():
	map_table = {'.': 100, 'X': 5, 'O': 7, 'T': 35}

	results = []

	#source = io.open("A-small-attempt0.in", "r")
	source = io.open("A-Large.in", "r")

	testcase_count = int(source.readline())
	for i in range(testcase_count):
		board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
		has_empty_cell = False
		for row in range(4):
			content = source.readline()
			for col in range(4):
				board[row][col] = map_table[content[col]]
				if board[row][col] == 100:
					has_empty_cell = True
		# skip the last empty line
		source.readline()

		""" for debug
		for col in range(len(board)):
			line = ""
			for row in range(len(board[col])):
				line += "{0:03d} ".format(board[col][row])
			print(line)
			print("")
		"""

		has_a_winner = False

		# check col win
		for row in range(4):
			sum = board[row][0] + board[row][1]+ board[row][2] + board[row][3]
			result = check_result(sum)
			if result > 0:
				results.append("Case #{0}: X won".format(i + 1))
				has_a_winner = True
				break
			elif result < 0:
				results.append("Case #{0}: O won".format(i + 1))
				has_a_winner = True
				break

		if has_a_winner:
			continue

		# check row win
		for col in range(4):
			sum = board[0][col] + board[1][col] + board[2][col] + board[3][col]
			result = check_result(sum)
			if result > 0:
				results.append("Case #{0}: X won".format(i + 1))
				has_a_winner = True
				break
			elif result < 0:
				results.append("Case #{0}: O won".format(i + 1))
				has_a_winner = True
				break

		if has_a_winner:
			continue

		# check diagonal win
		sum = board[0][0] + board[1][1] + board[2][2] + board[3][3]
		result = check_result(sum)
		if result > 0:
			results.append("Case #{0}: X won".format(i + 1))
			continue
		elif result < 0:
			results.append("Case #{0}: O won".format(i + 1))
			continue

		sum = board[3][0] + board[2][1] + board[1][2] + board[0][3]
		result = check_result(sum)
		if result > 0:
			results.append("Case #{0}: X won".format(i + 1))
			continue
		elif result < 0:
			results.append("Case #{0}: O won".format(i + 1))
			continue

		if has_empty_cell:
			results.append("Case #{0}: Game has not completed".format(i + 1))
		else:
			results.append("Case #{0}: Draw".format(i + 1))

	with io.open("A-large.out", "w", encoding="utf-8") as f:
		for i in range(len(results)):
			f.write(results[i])
			if i != len(results) - 1:
				f.write('\n')

if __name__ == "__main__":
	main()
