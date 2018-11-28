import sys,logging

#logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

inputFile = open(sys.argv[1])
outFile   = open("outFile.txt", "w")
for i in range(int(inputFile.readline())):
	input = []
	for j in range(4):
		input.append([])
		for c in inputFile.readline().rstrip():
			input[j].append(c)
	inputFile.readline()

	winner = "none"
	incomplete = False 
	
	############# CASE 1 ##############
	for j in range(4):
		player = ""
		if winner != "none":
			continue
		for k in range(4):
			inp = input[j][k]
			if inp == "T":
				continue
			elif inp == ".":
				player = "none"
				incomplete = True 
			elif player == "":
				player = inp
			elif player != inp: 
				player = "none"
				continue
		winner = player
		
	logging.debug(winner)
	############# CASE 2 ##############
	for j in range(4):
		player = ""
		if winner != "none":
			continue
		for k in range(4):
			inp = input[k][j]
			if inp == "T":
				continue
			elif inp == ".":
				player = "none"
				incomplete = True 
			elif player == "":
				player = inp
			elif player != inp: 
				player = "none"
				continue
		winner = player

	logging.debug(winner)
	############# CASE 3 ##############
	player = ""
	for j in range(4):
		if winner != "none":
			continue
		inp = input[j][j]
		if inp == "T":
			continue
		elif inp == ".":
			player = "none"
			incomplete = True 
		elif player == "":
			player = inp
		elif player != inp: 
			player = "none"
			continue
	if winner == "none":
		winner = player

	logging.debug(winner)
	############# CASE 4 ##############
	player = ""
	for j in range(4):
		if winner != "none":
			continue
		inp = input[j][3-j]
		if inp == "T":
			continue
		elif inp == ".":
			player = "none"
			incomplete = True 
		elif player == "":
			player = inp
		elif player != inp: 
			player = "none"
			continue

	logging.debug(winner)

	if winner == "none":
		winner = player
	
	if winner == "none":
		if incomplete:
			outFile.write("Case #" + str(i+1) + ": Game has not completed\n")
		else:
			outFile.write("Case #" + str(i+1) + ": Draw\n")
	else:
		outFile.write("Case #" + str(i+1) + ": " + winner + " won\n")

