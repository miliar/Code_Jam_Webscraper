import re
from collections import OrderedDict

lineNumb = 0;
def rounNum(pile, maxFlip):
	num = 0

	while(1):
		if(pile == None):
			return num
		print "pile" + pile 

		if(pile[0] == "+"):
	 		matchObj = re.match( '\++(-.*)?', pile, re.M|re.I)
	 		pile = matchObj.group(1)

		if (len(pile) < int(maxFlip)):
			return "IMPOSSIBLE"


		pilelist = list(pile)
		evalset = pilelist[0:int(maxFlip)]
		print evalset

		for n in range(int(maxFlip)):
			if(evalset[n] == '-'):
				pilelist[n] = '+'
			else:
				pilelist[n] = '-'
		num = num + 1
		pile = "".join(pilelist)
		print pile
		matchObj = re.match( '\++(-.*)?', pile, re.M|re.I)
		if(re.search( '\++(-.*)?', pile)):
			pile = matchObj.group(1)
		else:
			pile = ""
	


def evaluate (pile, iteration):

	maxFlip = pile.split()[1]
	pile = pile.split()[0]

	out_file = open("A-large.out","a")
	matchObj = re.match( '(.*-)?', pile, re.M|re.I)

	if(re.search( '(.*-)?', pile)):
		roundNum = rounNum(matchObj.group(1), maxFlip)
		out_file.write("Case #" + str(iteration) + ": " + str(roundNum) + "\n")
	else:
		out_file.write("Case #" + str(iteration) + ": 0\n" )

	out_file.close()

with open("A-large.in") as file:
	iteration = 0
	for line in file:
		if(lineNumb == 0):
			lineNumb = line
		else:
			evaluate(line.strip('\n'), iteration)
		iteration = int(iteration) + 1