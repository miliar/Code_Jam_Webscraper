import sys,os
import datetime 

def check_winner(pattern):
	winner = ""
	pattern_x = (
		"XXXX",
		"XXXT",
		"XXTX",
		"XXTT",
		"XTXX",
		"XTXT",
		"XTTX",
		"XTTT",
		"TXXX",
		"TXXT",
		"TXTX",
		"TXTT",
		"TTXX",
		"TTXT",
		"TTTX",
	)
	pattern_o = (
		"OOOO",
		"OOOT",
		"OOTO",
		"OOTT",
		"OTOO",
		"OTOT",
		"OTTO",
		"OTTT",
		"TOOO",
		"TOOT",
		"TOTO",
		"TOTT",
		"TTOO",
		"TTOT",
		"TTTO",
	)

	if pattern[0] == "X":
		if pattern in pattern_x:
			print "X-win"
			winner = "X"
	elif pattern[0] == "T":
		if pattern in pattern_x:
			print "X-win"
			winner = "X"
		elif pattern in pattern_o:
			print "O-win"
			winner = "O"
	elif pattern[0] == "O":
		if pattern in pattern_o:
			print "O-win"
			winner = "O"

	return winner


if __name__ == "__main__":
	is_firstline = True
	num_of_cases = 0
	case = 1
	row = 0
	blank_board = [
				 "....",
				 "....",
				 "....",
				 "...."
				]

	cur_board = list(blank_board)
	infile = open("input.txt","r")
	outfile = open("output.txt","w")
	# "N'-> Space found and the game might not end yet, "" is wildcard flag, not being used
	board_result = {"X":False,"O":False,"N":False,"":False} 

	
	for line in infile:
		if is_firstline:
			num_of_cases = int(line)
			is_firstline = False
		elif len(str(line)) > 1:
			# Record board status
			cur_board[row] = line.strip("\n")
			row = row + 1

		else:
			# Calculate the latest board result before go to next board
			for i in range(0,4):
				# Check horizontal pattern 4 rows
				row_str = str(cur_board[i])
				winner = check_winner(row_str)
				board_result[winner] = True

				# Check space ('.') in board 4 columns
				if row_str.find('.') > 0:
					board_result["N"] = True

				# Check vertical patterns
				col_str = str(cur_board[0][i]+cur_board[1][i]+cur_board[2][i]+cur_board[3][i])
				winner = check_winner(col_str)
				board_result[winner] = True

			# Check diagonal pattern 2 corners
			ldiag_str = str(cur_board[0][0]+cur_board[1][1]+cur_board[2][2]+cur_board[3][3])
			rdiag_str = str(cur_board[0][3]+cur_board[1][2]+cur_board[2][1]+cur_board[3][0])
			winner = check_winner(ldiag_str)
			board_result[winner] = True
			winner = check_winner(rdiag_str)
			board_result[winner] = True

			# Summarize result
			if board_result["O"]:
				outfile.write("Case #"+str(case)+": O won\n")
			elif board_result["X"]:
				outfile.write("Case #"+str(case)+": X won\n")
			elif board_result["N"] or (cur_board == blank_board): #and (board_result["O"] == False and board_result["X"] == False):
				outfile.write("Case #"+str(case)+": Game has not completed\n")
			elif not board_result["N"]: #and board_result["O"] == False and board_result["X"] == False:
				outfile.write("Case #"+str(case)+": Draw\n")

			# Clear all board for calculating next board's result
			cur_board = list(blank_board)
			row = 0
			case = case + 1
			board_result = {"X":False,"O":False,"N":False,"":False}


	infile.close()
	outfile.close()
