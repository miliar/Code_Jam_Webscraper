import fileinput
rows = []
formatted_cards = []
cards = []
for line in fileinput.input():
	line = line.strip()
	if fileinput.isfirstline():
		cases = int(line)
	else:
		if (fileinput.lineno() - 2) % 5 == 0:
			formatted_cards.append(cards)
			cards = []
			rows.append(int(line)-1)
		else:
			cards.append(set([int(card) for card in line.split(" ")]))

formatted_cards.append(cards)
formatted_cards = formatted_cards[1:]

for case in range(cases):
	p1 = formatted_cards[case*2][rows[case*2]]
	p2 = formatted_cards[case*2+1][rows[case*2+1]]
	possible_cards = p1 & p2
	print "Case #"+str(case+1)+":",
	if len(possible_cards) == 0:
		print "Volunteer cheated!"
	elif len(possible_cards) == 1:
		print list(possible_cards)[0]
	else:
		print "Bad magician!"



