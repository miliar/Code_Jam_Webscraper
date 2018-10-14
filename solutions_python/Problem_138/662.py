#author : Matt Toal
import sys

sys.setrecursionlimit(2000)
def parseLine(line):
	return [float(x) for x in line.split(" ")]


def parseInput(fileName):
	with open(fileName,"r") as f:
		firstLine = True
		inputLineNumber = 0
		case = 0
		with open("problem4answers.txt","w") as g:
			for line in f:
				if not firstLine:
					if inputLineNumber == 0:
						case += 1
						inputLineNumber +=1
					elif inputLineNumber == 1:
						myTiles = parseLine(line)
						inputLineNumber +=1
					elif inputLineNumber == 2:
						hisTiles = parseLine(line)
						inputLineNumber = 0
						(fair, cheat) = scores(myTiles, hisTiles)
						printAnswer(g,fair,cheat,case)
				else:
					firstLine= False

def scores(myTiles,hisTiles):
	fairScore = getFairScore(sorted(myTiles),sorted(hisTiles))
	cheatScore = getCheatScore(sorted(myTiles),sorted(hisTiles))
	return (fairScore, cheatScore)

def getFairScore(myTiles,hisTiles):
	if len(myTiles) == 0:
		return 0
	myPlay = myTiles[-1]
	if myPlay > hisTiles[-1]:
		return getFairScore(myTiles[:-1], hisTiles[1:]) + 1
	else:
		hisNewTiles = getHisRemainingTiles(myPlay,hisTiles)
		return getFairScore(myTiles[:-1], hisNewTiles)

def getCheatScore(myTiles, hisTiles):
	if len(myTiles) == 0:
		return 0
	if myTiles[-1] > hisTiles[-1]:
		return getCheatScore(myTiles[:-1],hisTiles[:-1]) + 1
	else:
		return getCheatScore(myTiles[1:], hisTiles[:-1])


def getHisRemainingTiles(myPlay,hisTiles):
	for hisTile in hisTiles:
		if hisTile > myPlay:
			hisTiles.remove(hisTile)
			return hisTiles




def printAnswer(g, fair, cheat, t):
	g.write("Case #" + str(t) + ": " + str(cheat) + " " + str(fair) + "\n")

def main(argv=None):
	if argv == None:
		argv = sys.argv
	if len(argv) > 1:
		parseInput(argv[1])
if  __name__ == "__main__":
	main()
