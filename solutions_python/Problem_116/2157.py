# Coded in python 3.3

import pprint

INPUT_FILE = "A-large.in"
OUTPUT_FILE = "tictac_output.txt"


def parseInput():
	"""
	Returns a list of lists containing a game state based on input file
	for every game state.
	That means that every 4 lists, there will be a new state.
	Parsed:
	 0 = nothing
	 1 = X
	 2 = O
	 3 = ?
	"""
	returnList = []

	with open(INPUT_FILE, "r") as fd:
		first = True
		for line in fd:
			if first:
				first = False
				continue
			subList = []
			for char in line:
				if char == "X":
					subList.append(1)
				elif char == "O":
					subList.append(2)
				elif char == ".":
					subList.append(0)
				elif char == "T":
					subList.append(3)
				elif char == "\n":
					pass
				else:
					raise ValueError("Invalid char", char)
			if len(subList) > 1:
				returnList.append(subList)

	return returnList









def printList(list):
	print(pprint.pformat(list))

if __name__ == "__main__":
	parsedList = parseInput()

	#print(pprint.pformat(parsedList))
	# print(len(parsedList))
	
	fd = open(OUTPUT_FILE, "w")
	n = 1
	for i in range ( 0, len(parsedList), 4):
		
		xWon = False
		oWon = False
		draw = False
		won = False
		completed = True

		# Check lateral win		
		for j in range(4):
			nSame = 0
			type = None
			if parsedList[i+j][0] != 3:
				k = 0
				type = parsedList[i+j][0]
			else:
				k = 1
				type = parsedList[i+j][1]
			if parsedList[i+j][0] == parsedList[i+j][1]:
				nSame += 1
			if parsedList[i+j][1] == parsedList[i+j][2]:
				nSame += 1
			if parsedList[i+j][2] == parsedList[i+j][3]:
				nSame += 1
			if parsedList[i+j][0] == parsedList[i+j][3]:
				nSame += 1
			# if parsedList[i+j][k] == parsedList[i+j][3]:
			# 	nSame += 1
			# if parsedList[i+j][k] == parsedList[i+j][4]:
			# 	nSame += 1
			tFound = False
			voidFound = False
			for l in range(4):
				if parsedList[i+j][l] == 3:
					tFound = True
				if parsedList[i+j][l] == 0:
					voidFound = True

			if not voidFound and ((tFound and nSame == 2) or (not tFound and nSame == 4)):
				won = type

		# Check for transversal win
		if not won:
			for j in range(4):
				nSame = 0
				type = None
				if parsedList[i][j] != 3:
					k = 0
					type = parsedList[i][j]
				else:
					k = 1
					type = parsedList[i+1][j]
				if parsedList[i][j] == parsedList[i+1][j]:
					nSame += 1
				if parsedList[i+1][j] == parsedList[i+2][j]:
					nSame += 1
				if parsedList[i+2][j] == parsedList[i+3][j]:
					nSame += 1
				if parsedList[i][j] == parsedList[i+3][j]:
					nSame += 1
				# if parsedList[i][j] == parsedList[i+3][j]:
				# 	nSame += 1

				tFound = False
				voidFound = False
				for l in range(4):
					if parsedList[i+l][j] == 3:
						tFound = True
					if parsedList[i+l][j] == 0:
						voidFound = True

				if not voidFound and ((tFound and nSame == 2) or (not tFound and nSame == 4)):
					won = type

		# Check for top left to bottom right diagonal win
		if not won:
			nSame = 0
			type = None
			if parsedList[i][0] != 3:
				type = parsedList[i][0]
			else:
				type = parsedList[i+1][1]

			# print( "parseDList", parsedList[i+0][0], parsedList[i+1][1])
			if parsedList[i+0][0] == parsedList[i+1][1]:
				nSame += 1
			if parsedList[i+1][1] == parsedList[i+2][2]:
				nSame += 1
			if parsedList[i+2][2] == parsedList[i+3][3]:
				nSame += 1
			if parsedList[i+0][0] == parsedList[i+3][3]:
				nSame += 1
			# if parsedList[i+k][k+3] == parsedList[i+3][3] and k != 0:
			# 	nSame += 1
			# print("nsame",nSame)
			tFound = False
			voidFound = False
			for l in range(4):
				if parsedList[i+l][l] == 3:
					tFound = True
				if parsedList[i+l][l] == 0:
					voidFound = True

			if not voidFound and ((tFound and nSame == 2) or (not tFound and nSame == 4)):
				won = type

		# Check for top right to bottom left diagonal win
		if not won:
			nSame = 0
			type = None
			if parsedList[i][3] != 3:
				type = parsedList[i][3]
			else:
				type = parsedList[i+1][2]

			# print( "parseDList", parsedList[i+0][0], parsedList[i+1][1])
			if parsedList[i+0][3] == parsedList[i+1][2]:
				nSame += 1
			if parsedList[i+1][2] == parsedList[i+2][1]:
				nSame += 1
			if parsedList[i+2][1] == parsedList[i+3][0]:
				nSame += 1
			if parsedList[i+0][3] == parsedList[i+3][0]:
				nSame += 1
			# if parsedList[i+k][k+3] == parsedList[i+3][3] and k != 0:
			# 	nSame += 1
			# print("nsame",nSame)
			tFound = False
			voidFound = False
			for l in range(4):
				if parsedList[i+l][3-l] == 3:
					tFound = True
				if parsedList[i+l][3-l] == 0:
					voidFound = True

			if not voidFound and ((tFound and nSame == 2) or (not tFound and nSame == 4)):
				won = type

		# Check for completion
		j = i - 1
		while (completed and j < i + 3):
			j += 1
			for l in range(4):
				if parsedList[j][l] == 0:
					completed = False

		string = ""
		# print(won)
		if won == 1:
			string = "X won"
		elif won == 2:
			string = "O won"
		elif won != False:
			raise ValueError(won)
		elif not completed:
			string = "Game has not completed"
		else:
			string = "Draw"
		string = "Case #" + str(n) + ": " + string
		if not i + 4 == len(parsedList):
			string += "\n"
		fd.write(string)
		n += 1
	fd.close()
