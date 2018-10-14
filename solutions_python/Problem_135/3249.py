import sys
def processFile(filename):
	in_file = open(filename,"r")
	number_of_games = int(in_file.readline())
	#for each game
	for game_index in range(number_of_games):
		possible_cards = []
		#for each board in the game
		for i in range(2):
			row_selected = int(in_file.readline())-1
			#for each row on the board
			for row_index in range(4):
				this_line = in_file.readline().split()
				this_line = map(int,this_line)
				if row_index==row_selected:
					possible_cards.append(this_line)
		possible_cards = list(set(possible_cards[0]) & set(possible_cards[1]))
		out_text=""
		if len(possible_cards) == 0:
			out_text = "Volunteer cheated!"
		elif len(possible_cards) == 1:
			out_text = str(possible_cards[0])
		else:
			out_text = "Bad magician!"
		string = "Case #"+str(game_index+1)+": "+out_text
		print string

		
	return in_file

if __name__ == "__main__":
	processFile("A-small-attempt0.in")
