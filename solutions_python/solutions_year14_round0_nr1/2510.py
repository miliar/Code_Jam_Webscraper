def check_cards(deck,p_deck,case):
	deck = [int(x) for x in deck]
	p_deck = [int(x) for x in p_deck]
	cards = list()
	for card in deck:
		if card in p_deck:
			cards.append(card)

	if len(cards)==0:
		return "Case #{}: Volunteer cheated!".format(case+1)
	elif len(cards)==1:
		return "Case #{}: {}".format(case+1,cards[0])
	else:
		return "Case #{}: Bad magician!".format(case+1)

inp = open('input.dat','r')
out = open('output.dat','w')

for case in xrange(int(inp.readline())):

	magic_row = int(inp.readline())
	
	for discard in xrange(magic_row-1):
		inp.readline()
	
	posible_cards = inp.readline().split(" ")
	
	for discard in xrange(4-magic_row):
		inp.readline()
	
	magic_row = int(inp.readline())

	for discard in xrange(magic_row-1):
		inp.readline()

	magic_cards = inp.readline().split(" ")

	for discard in xrange(4-magic_row):
		inp.readline()

	if case!=0:
		out.write('\n')

	out.write(check_cards(posible_cards,magic_cards,case))

inp.close()
out.close()