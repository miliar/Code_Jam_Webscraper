#!/usr/bin/env python
# -*- coding: utf-8 -*-

def parse(inFile):
    row1 = int(inFile.readline())
    spread1 = [(inFile.readline().split()) for z in xrange(4)]
    row2 = int(inFile.readline())
    spread2 = [(inFile.readline().split()) for z in xrange(4)]
    return [row1, spread1, row2, spread2]

def solve(data):
    TOO_MANY = "Bad magician!"
    NO_CARDS = "Volunteer cheated!"

    row1 = data[0]
    spread1 = data[1]
    row2 = data[2]
    spread2 = data[3]

    cards = set(spread1[row1 - 1])&set(spread2[row2 - 1]) 
    if len(cards) == 1:
	card = cards.pop()
	return str(card)
    if len(cards) > 1:
	card = TOO_MANY
    if len(cards) == 0:
	card = NO_CARDS
    # result = 'card: {} cards: {} row1: {} spread1: {} row2: {} spread2: {}'.format(card, cards, row1, spread1, row2, spread2)
    return card

if __name__ == "__main__":
    from GCJ import GCJ
    GCJ(parse, solve, "/home/lynoure/GCJdata", "A").run()

