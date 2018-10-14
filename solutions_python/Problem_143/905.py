#author : Matt Toal
import sys

def parseLine(line):
	inputLine = line.split(" ")
	c = int(inputLine[0])
	f = int(inputLine[1])
	x = int(inputLine[2])
	return (c, f, x)


def parseInput(fileName):
	with open(fileName,"r") as f:
		firstLine = True
		case = 0
		with open("problem2answers.txt","w") as g:
			for line in f:
				if not firstLine:
					(a,b,k) = parseLine(line)
					wins = solve(a,b,k)
					printAnswer(case, wins, g)
				else:
					firstLine= False
				case +=1

def printAnswer(t, answer,g):
	g.write("Case #" + str(t) + ": " + str(answer) + "\n")


def solve(a,b,k):
	ans=0
	for i in xrange(a):
		for j in xrange(b):
			if i & j < k:
				ans +=1

	return ans

def main(argv=None):
	if argv == None:
		argv = sys.argv
	if len(argv) > 1:
		parseInput(argv[1])
if  __name__ == "__main__":
	main()
