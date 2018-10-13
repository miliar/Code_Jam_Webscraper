import sys

def output(rows):
	if len(rows) == 1:
		return rows.pop()
	elif len(rows) == 0:
		return "Volunteer cheated!"
	else:
		return "Bad Magician!"


def parseInput(fileName):
	with open(fileName,"r") as f:
		inputLines = f.readlines()
	arrangment1=[]
	arrangment2=[]
	inputLines = inputLines[1:]
	t=0
	with open("problem1answers.txt","w") as g:
		while len(inputLines) != 0:
			t+=1
			case = inputLines[:10]
			inputLines = inputLines[10:]
			line1 = setFromLine(case[0:5][int(case[0])])
			print line1
			line2 = setFromLine(case[5:10][int(case[5])])
			print line2
			answer = output(line1 & line2)
			printAnswer(g,answer,t)

def printAnswer(g, answer, t):
	g.write("Case #" + str(t) + ": " + answer + "\n")

def setFromLine(line):
	return set(line.strip().split(" "))


def main(argv=None):
	if argv == None:
		argv = sys.argv
	if len(argv) > 1:
		parseInput(argv[1])
	else:
		print "usage: python experimentCleanup.py ####"
if  __name__ == "__main__":
	main()
