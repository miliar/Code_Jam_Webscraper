#!/usr/bin/env python

n = int(raw_input())
for i in range(n):
	first_guess = int(raw_input())-1
	square1 = []
	for j in range(4):
		square1.append(map(int,raw_input().strip().split()))
	first_guess_row = square1[first_guess]

	second_guess = int(raw_input())-1
	square2 = []
        for j in range(4):
                square2.append(map(int,raw_input().strip().split()))
	second_guess_row = square2[second_guess]

	card = set(first_guess_row) & set (second_guess_row)
	if len(card) == 1:
		print "Case #"+str(i+1)+": "+ str(list(card)[0])
	elif len(card) > 1:
		print "Case #"+str(i+1)+": Bad magician!"
	else :
		print "Case #"+str(i+1)+": Volunteer cheated!"


	
		
