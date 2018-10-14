def getint ():
	return int(raw_input())

def printCase(c, s):
	print "Case #" + str(c) + ": " + str(s)

def intersection (list1, list2):
	first = set (list1)
	second = set (list2)
	return list(first.intersection(second))

def getPossibleCards (rows1, choice1, rows2, choice2):
	firstpos = rows1[(choice1 - 1) * 4 : (choice1) * 4];
	return intersection(firstpos, rows2[(choice2 - 1) * 4 : (choice2) * 4]);

for i in range(getint()):
	a1 = getint();
	rows1 = raw_input() + " " + raw_input() + " " + raw_input() + " " + raw_input()
	a2 = getint();
	rows2 = raw_input() + " " + raw_input() + " " + raw_input() + " " + raw_input()
	pcards = getPossibleCards(rows1.split(" "), a1, rows2.split(" "), a2)

	if len(pcards) == 0:
		printCase(i+1,"Volunteer cheated!")
	elif len(pcards) == 1:
		printCase(i+1,pcards[0])
	else:
		printCase(i+1,"Bad magician!")