# -*- coding: utf-8 -*-
import os.path

filename = "A-Tic-Tac-Toe-Tomek-large"
inputfilename = os.path.join("input", filename)
outputfilename = os.path.join("output", filename)

def main():
	inputfile = open(inputfilename)
	totalinputcount = int(inputfile.readline())
	outputfile = open(outputfilename, "w+")
	for i in range(totalinputcount):
		currentgame = []
		for j in range(4):
			currentgame.append(inputfile.readline().strip())
		inputfile.readline() # empty line
		# print currentgame
		if CheckHorizontal(currentgame, "O") or CheckVertical(currentgame, "O") or CheckDiagonal(currentgame, "O"):
			outputfile.write("Case #%s: O won\n" % str(i+1))
		elif CheckHorizontal(currentgame, "X") or CheckVertical(currentgame, "X") or CheckDiagonal(currentgame, "X"):
			outputfile.write("Case #%s: X won\n" % str(i+1))
		elif not CheckIfFinished(currentgame):
			outputfile.write("Case #%s: Game has not completed\n" % str(i+1))
		else:
			outputfile.write("Case #%s: Draw\n" % str(i+1))
	inputfile.close()
	outputfile.close()
	pass

def CheckHorizontal(game, keytocheck):
	for i in range(4):
		for j in range(4):
			if game[i][j] != keytocheck and game[i][j] != "T":
				break
		else:
			return True
	return False

def CheckVertical(game, keytocheck):
	for i in range(4):
		for j in range(4):
			if game[j][i] != keytocheck and game[j][i] != "T":
				break
		else:
			return True
	return False

def CheckDiagonal(game, keytocheck):
	for i in range(4):
		if game[i][i] != keytocheck and game[i][i] != "T":
			break
	else:
		return True	
	for i in range(4):
		if game[i][3-i] != keytocheck and game[i][3-i] != "T":
			break
	else:
		return True
	return False

def CheckIfFinished(game):
	game = "".join("".join(game))
	if "." in game:
		return False
	return True

if __name__ == '__main__':
	main()
	pass