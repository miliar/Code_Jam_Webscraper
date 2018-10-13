lineNumber = 0
cards = []
result = []
for line in open("A-small-attempt0.in"):
	lineNumber += 1

	if lineNumber == 1:
		continue;

	if (lineNumber - 2) % 5 == 0:
		secondChoice = int(line)
		cards = []

		if (lineNumber - 2) % 10 == 0:
			firstChoice = int(line)
			secondChoice = 0

		continue;

	cards.append(map(lambda x: int(x.strip()), line.split(" ")))
	if len(cards) == 4:
		if secondChoice == 0:
			firstChoiceCards = cards[firstChoice - 1]
		else:
			secondChoiceCards = cards[secondChoice - 1]
			commonCards = set(firstChoiceCards) & set(secondChoiceCards)
			print(firstChoiceCards, secondChoiceCards, commonCards)
			if len(commonCards) == 1:
				result.append(commonCards.pop())
			elif len(commonCards) == 0:
				result.append("Volunteer cheated!")
			else:
				result.append("Bad magician!")

	print("cards: %s" % cards)
	print("firstChoice: %s" % firstChoice)
	print("secondChoice: %s" % secondChoice)
	print(result)

output = open("output.txt", "w")
for i in range(len(result)):
	output.write("Case #%s: %s\n" % (i + 1, result[i]))

