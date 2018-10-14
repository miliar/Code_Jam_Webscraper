num_tests = int(raw_input())
output = ""
for i in range(num_tests):
	total_moves = 0
	data = raw_input().rsplit(' ')
	num_buttons = int(data[0])
	bot_blue = 1 # current location of the blue bot
	bot_orange = 1 # current location of orange bot
	buf_orange = 0 # number of moves that blue bot took before orange can move
	buf_blue = 0
	for j in range(1, len(data), 2):
		hallway = data[j]
		button = int(data[j+1])
		# need to move the bot to the button
		if hallway == 'O':
			# move orange bot
			moves = abs(bot_orange - button) - buf_orange
			if moves < 0:
				moves = 0
			moves += 1
			buf_orange = 0
			buf_blue += moves
			total_moves += moves
			bot_orange = button
		elif hallway == 'B':
			# move blue bot
			moves = abs(bot_blue - button) - buf_blue
			if moves < 0:
				moves = 0
			moves += 1
			buf_blue = 0
			buf_orange += moves
			total_moves += moves
			bot_blue = button
	output += "Case #" + str(i+1) + ": " + str(total_moves) + "\n"
print output
