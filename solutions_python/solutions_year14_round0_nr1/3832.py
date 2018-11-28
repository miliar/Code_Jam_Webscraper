#!/usr/bin/env python

import sys

# globals
result = []


# get test count
test_count = int(raw_input())

if test_count>100 or test_count<1:
	print "Test Count input out of bounds. Should be between 1 and 100 only"
	sys.exit()

# compute for result
def check_for_the_number(rows):

	Number = []

	for number in rows[0]:
		if number in rows[1]:
			Number.append(number)

	if len(Number) > 1:
		result.append("Bad magician!")
	elif len(Number) < 1:
		result.append("Volunteer cheated!")
	else:
		result.append(Number[0])


# check for card number integrity
def has_duplicate(card_row, all_cards):
	for i in card_row:
		if i in all_cards:
			return True
	return False


# get input per test
while test_count:
	
	set_of_cards = 2
	rows = []

	# test cases 
	while set_of_cards:

		# row number
		row_number = int(raw_input())
		cards = []

		if row_number>4 or row_number<1:
			print "row number out of bounds, please enter 1 to 4 only"
			continue

		# set of cards
		for i in range(0, 4):

			new_set = map(int, raw_input().split(" "))

			if max(new_set) > 16 or 0 in new_set:
				print "Card is out of bounds it must be between 1 and 16 only"
				sys.exit()

			if has_duplicate(new_set, cards):
				print "You have duplicate cards"
				sys.exit()

			cards.extend(new_set)
			
			if row_number == i+1:
				rows.append(new_set)

		set_of_cards -= 1

	if len(rows) != 2:
		sys.exit()

	check_for_the_number(rows)
	test_count -= 1

# output
for i in range(0, len(result)):
	print "Case #%d: %s" % (i+1, result[i])