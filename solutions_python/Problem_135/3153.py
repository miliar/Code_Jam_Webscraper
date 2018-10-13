#!/usr/bin/python
import sys
import os

class cardTrick(object):
	test_cases = 0
	
	def __init__(self, cardRow1, cardRow2, cards1, cards2):
		self.cardRow1 = cardRow1
		self.cardRow2 = cardRow2
		self.cards1 = cards1
		self.cards2 = cards2
	
	def guess(self):
		set1 = set(self.cards1[self.cardRow1-1])
		set2 = set(self.cards2[self.cardRow2-1])
		guess = set1 & set2
		if(len(guess) == 1):
			return str(guess.pop())
		elif(len(guess) == 0):
			return "Volunteer cheated!"
		else:
			return "Bad magician!"

		
def get_input():
	if(len(sys.argv) < 2):
		print "No filename specified.\nUsage: python " + sys.argv[0] + " filename"
	filename = sys.argv[1]
	if(os.path.isfile(filename)):
		return open(sys.argv[1], 'r')
	else:
		print "file " + filename + " not found."
	exit()
		
		
def parse_input(input):
	global test_cases
	test_cases = int(input.readline())
	cardTricks = []
	for x in range(0, test_cases):
		cardRow1 = int(input.readline())
		cards1 = []
		for i in range(0, 4):
			cards1.append(input.readline().split())
		cardRow2 = int(input.readline())
		cards2 = []
		for i in range(0, 4):
			cards2.append(input.readline().split())		
		cardTricks.append(cardTrick(cardRow1, cardRow2, cards1, cards2))
	return cardTricks
		
input = get_input()
cardTricks = parse_input(input)
for x in range(0, test_cases):
	print "Case #" + str(x + 1) + ": " + cardTricks[x].guess()