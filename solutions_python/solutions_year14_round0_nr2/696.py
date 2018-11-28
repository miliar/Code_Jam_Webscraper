#author : Matt Toal
import sys

def buy(c,f,x,r):
	return c < x and (noBuyTimeLeft(c,x,r) > buyTimeLeft(f,x,r))

def buyTimeLeft(f,x,r):
	return x/(r+f)

def noBuyTimeLeft(c,x,r):
	return (x-c)/r

def parseLine(line):
	inputLine = line.split(" ")
	c = float(inputLine[0])
	f = float(inputLine[1])
	x = float(inputLine[2])
	return (c, f, x)

def timeToWin(c,f,x,r,t):
	if not buy(c,f,x,r):
		return x/r
	else:
		return  timeToWin(c,f,x,r+f, t + (c/r))

def timeToWinStep(c,f,x,r,t):
	if not buy(c,f,x,r):
		return [-1, 0, 0, 0, t + x/r]
	else:
		return [c,f,x,r+f, t + (c/r)]

def parseInput(fileName):
	with open(fileName,"r") as f:
		firstLine = True
		case = 0
		with open("problem2answers.txt","w") as g:
			for line in f:
				if not firstLine:
					(c,f,x) = parseLine(line)
					r = 2.0
					t = 0
					while c != -1:
						[c,f,x,r,t] = timeToWinStep(c,f,x,r,t)
					printAnswer(g,t,case)
				else:
					firstLine= False
				case +=1

def printAnswer(g, answer, t):
	g.write("Case #" + str(t) + ": " + str(answer) + "\n")

def main(argv=None):
	if argv == None:
		argv = sys.argv
	if len(argv) > 1:
		parseInput(argv[1])
if  __name__ == "__main__":
	main()
