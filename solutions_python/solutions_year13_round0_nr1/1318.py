#!/usr/bin/python
import fileinput
#import time

line_number = 0
#f = 'sample_input.txt'
#f = 'A-small-attempt0.in'
f = 'A-large.in'


def check_win(game_str):
	potential_test = []

	#collect the rows first
	for i in xrange(4):
		potential_test.append(game_str[(i*4):((i+1)*4)])
	#collect the columns
	for i in xrange(4):
		column_str = ""
		for j in xrange(4):
			column_str += game_str[i+j*4]
		potential_test.append(column_str)
	#diagonals
	diagonal_str = ""
	diagonal2_str = ""
	for i in xrange(4):
		diagonal_str += game_str[i+i*4]
		diagonal2_str += game_str[(3-i)+i*4]
	potential_test.append(diagonal_str)
	potential_test.append(diagonal2_str)
	
	#print potential_test

	x_win = 0
	o_win = 0
	for test_str in potential_test:
		if (test_str.count('.') > 0):
			continue
		if (test_str.count('X') + test_str.count('T') == 4):
			x_win += 1
		if (test_str.count('O') + test_str.count('T') == 4):
			o_win += 1

	if (x_win > o_win):
		return "X won"
	elif (o_win > x_win):
		return "O won"
	elif ((x_win == o_win) and game_str.count('.') == 0):
		return "Draw"
	else:
		return "Game has not completed"


for line in open (f, 'r'):
        if line_number == 0:
                #this is the number of test case
                test_case_count = int(line)
		current_game = ""
        elif (line_number/5) <= test_case_count:
		line_mod_5 = line_number%5
		if (line_mod_5 > 0):
			current_game += line.strip()	

		else:
			#print current_game
			print "Case #"+str(line_number/5)+": "+check_win(current_game)
			current_game = ""



        line_number = line_number + 1

