#!/usr/bin/python

def get_trick_input():
	guess = int(raw_input())
	row = []
	for i in range(1, 5):
		if i == guess:
			row = raw_input().split(" ")
		else:
			raw_input()

	return guess, row

for case in range(1,int(raw_input())+1):          #For all test cases

	first_guess, first_row = get_trick_input()
	second_guess, second_row = get_trick_input()

	possible_cards = list(set(first_row) & set(second_row))
	if (len(possible_cards) == 1):
		answer = str(possible_cards[0])
	elif (len(possible_cards) > 1):
		answer = "Bad magician!"
	else:
		answer = "Volunteer cheated!"

	print "Case #%d: %s" % (case, answer)

