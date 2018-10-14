test_input = r'''3
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 5 4
3 11 6 15
9 10 7 12
13 14 8 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16'''.split('\n')

def debug(s, s2=None):
	if s2 is not None:
		print s, s2
	else:
		print s

def readline():
	
	# return test_input.pop(0)
	return raw_input()

def case(casenum):
	cards = []
	
	# Which row is the card in?
	answer = int(readline())
	
	for i in xrange(4):
		line = readline()
		row = map(int, line.split())
		cards.append(row)
		
	chosenrow = set(cards[answer - 1])

	# Which row is the card in now?
	answer2 = int(readline()) 
	
	cards2 = []
	for i in xrange(4):
		line = readline()
		row = map(int, line.split())
		cards2.append(row)
		
	chosenrow2 = set(cards2[answer2 - 1])

	matches = chosenrow2.intersection(chosenrow)
	if len(matches) == 1:
		output = matches.pop()
	elif len(matches) > 1:
		output = "Bad magician!"
	else:
		output = "Volunteer cheated!"
	
	print "Case #%d: %s" % (casenum, output)
		

def main():
	numcases = readline()
	for i in xrange(int(numcases)):
		case(i + 1)

main()
