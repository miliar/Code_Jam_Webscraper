#magic trick

fr = open("A-small-attempt0.in", "r")
fw = open('A-small-attempt0.out', 'w')

def find_card(casenum, row1, row2):

	cards = []
	output = "Case #" + casenum + ": "
	for card1 in row1:
		possibleSoln = [card2 for card2 in (row2) if card2 == card1]
		cards.append(possibleSoln)

	# print "possibleSoln"
	# print possibleSoln

	has_result = []
	for possibleSoln in cards:
		if len(possibleSoln)	!= 0:
			has_result.append(possibleSoln)

	# print "has_result"
	# print has_result

	reslen = len(has_result)
	if reslen == 0:
		output += "Volunteer cheated!"
	elif reslen > 1:
		output += "Bad magician!"
	elif reslen == 1:
		output += has_result[0][0]

	output += "\n"

	fw.write(output)


def get_inp():

	T = int(fr.readline()[:-1]) #number of test cases

	for t in range(T):
		
		a1 = int(fr.readline()[:-1]) - 1
		grid1 = []
		for r in range(4):
			row = fr.readline()[:-1]
			row = row.split(" ")
			grid1.append(row)

		a2 = int(fr.readline()[:-1]) - 1
		grid2 = []
		for r in range(4):
			row = fr.readline()[:-1]
			row = row.split(" ")
			grid2.append(row)

		find_card(str(t+1), grid1[a1], grid2[a2])
		

get_inp()
fr.close()
fw.close()