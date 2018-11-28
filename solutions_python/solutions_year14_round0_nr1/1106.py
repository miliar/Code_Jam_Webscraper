content = open("A-small-attempt2.in","r").read().split("\n")
output = open("outtt.txt", "w")
cases = int(content[0])
posibleCards1 = []
passibleCards2 = []
cards = []
if cases > 100 or cases < 0:
	print "too large input"
j = 1
test = False
for i in range(0 , cases+cases-1):
	if test:
		test = False
		continue
	input1 = int(content[i*5+1])
	possibleCards1 = content[i*5+1+input1].split(" ")	
	input2 = int(content[(i+1)*5+1])
	possibleCards2 = content[(i+1)*5+1+input2].split(" ")
	cards = []
	for card in possibleCards1:
		if card in possibleCards2:
			cards.append(card)

	if len(cards) == 1:
		output.write("Case #{0}: {1}".format(j, cards[0]) + "\n")
	elif len(cards) > 1:
		output.write("Case #{0}: Bad magician!\n".format(j))
	else:
		output.write("Case #{0}: Volunteer cheated!\n".format(j))
	test = True
	j = j +1
	
