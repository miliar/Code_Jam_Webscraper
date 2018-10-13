import argparse


def solve(input_file, output_file):
	input_stream = open(input_file, "r")
	output_stream = open(output_file, "w")

	num = int(input_stream.readline().rstrip().lstrip())
	boards_done = 0

	def solve_board(board, t_line, boards_done):
		def print_result():
			output_stream.write("Case #" + str(boards_done + 1) + ": ")
			if has_winner:
				output_stream.write(winner + " won\n")
				print winner + " won\n"
			elif may_not_be_finished:
				output_stream.write("Game has not completed\n")
				print "Game has not completed\n"
			else:
				output_stream.write("Draw\n")
				print "Draw\n"

		print board
		if len(board) != 4:
			print "Board incomplete"

		may_not_be_finished = False
		has_winner = False
		winner = ""
		t_exists = t_line != -1

		line = board[t_line]
		probable_winner = ""


		# checks if there is horizontal winner
		for line in board:
			for char in line:
				if char == ".":
					may_not_be_finished == True
					break
				elif char == "T":
					continue
				elif not probable_winner:
					probable_winner = char
				elif char == probable_winner:
					continue
				else:
					break
			else:
				has_winner = True
				winner = probable_winner
				print_result()
				return

		# checks if there is vertical winner
		for index in range(0, 4):
			probable_winner = ""
			for line in board:
				chars = list(line)
				char = chars[index]

				if char == ".":
					may_not_be_finished == True
					break
				elif char == "T":
					continue
				elif not probable_winner:
					probable_winner = char
				elif char == probable_winner:
					continue
				else:
					break
			else:
				has_winner = True
				winner = probable_winner
				print_result()
				return

		#checks if there is a left to right diagonal winner
		index = 0
		probable_winner = ""
		for line in board:
			chars = list(line)
			char = chars[index]
			index = index + 1

			if char == ".":
				may_not_be_finished == True
				break
			elif char == "T":
				continue
			elif not probable_winner:
				probable_winner = char
			elif char == probable_winner:
				continue
			else:
				break
		else:
			has_winner = True
			winner = probable_winner
			print_result()
			return

		#checks if there is a right to left diagonal winner
		index = 3
		probable_winner = ""
		for line in board:
			chars = list(line)
			char = chars[index]
			index = index -1
			if char == ".":
				may_not_be_finished == True
				break
			elif char == "T":
				continue
			elif not probable_winner:
				probable_winner = char
			elif char == probable_winner:
				continue
			else:
				break
		else:
			has_winner = True
			winner = probable_winner
			print_result()
			return

		for line in board:
			chars = list(line)
			for char in chars:
				if char == ".":
					may_not_be_finished = True
					break
			else:
				continue
			break

		print_result()
		return

	while boards_done < num:
		board = []
		t_line = -1
		for i in range(0, 4):
			line = input_stream.readline().rstrip().lstrip()
			if "T" in line:
				t_line = i
			board.append(line)

		solve_board(board, t_line, boards_done)
		input_stream.readline()
		boards_done = boards_done + 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--in", dest="input_file")
    parser.add_argument("--out", dest="output_file")

    args = parser.parse_args()

    solve(args.input_file, args.output_file)
