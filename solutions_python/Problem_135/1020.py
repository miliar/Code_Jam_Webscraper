#! /usr/bin/env python2.7

T=int(raw_input())
for test in range(1,T+1):
	first_answer=int(raw_input())
	first_board=[]
	for i in range(4):
		row_text=raw_input()
		row_list=[int(card_nbr) for card_nbr in row_text.strip().split() ]
		first_board.append(row_list)
	
	second_answer=int(raw_input())
	second_board=[]
	for i in range(4):
		row_text=raw_input()
		row_list=[int(card_nbr) for card_nbr in row_text.strip().split() ]
		second_board.append(row_list)
	set_1=set(first_board[first_answer-1])
	set_2=set(second_board[second_answer-1])
	possible_answers=list(set_1 & set_2)
	if len(possible_answers)==0:
		print "Case #{}: Volunteer cheated!".format(test)
	elif len(possible_answers)==1:
		print "Case #{}: {}".format(test,possible_answers[0])
	else :
		print "Case #{}: Bad magician!".format(test)
		