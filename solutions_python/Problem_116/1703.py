#!/usr/bin/python

from __future__ import print_function
import sys

numInputs=int(sys.stdin.readline());
for n in range(numInputs):

	# read input into matrix
	board=[];
	for i in range(4):
		newRow = [];
		line = sys.stdin.readline();
		for j in range(4):
			newRow.append(line[j]);
		board.append(newRow);

	winner='';	
	gameOver=1;

	# first scan columns for winner
	for i in range(4):
		j=0;
		Ocnt=0;
		Xcnt=0;
		while (Ocnt==0 or Xcnt==0) and (j<4):
			ch = board[i][j];
			if ch == '.':
				gameOver=0;
				break;
			elif ch == 'O':
				Ocnt+=1;
			elif ch == 'X':
				Xcnt+=1;		
			j+=1;

		if j==4:
			if Ocnt==0:
				winner='X';
				break;
			elif Xcnt==0:
				winner='O';
				break;
			

	if not winner:			
		# now scan rows for winner
		for i in range(4):
			j=0;
			Ocnt=0;
			Xcnt=0;
			while (Ocnt==0 or Xcnt==0) and j<4:
				ch = board[j][i];
				if ch == '.':
					gameOver=0;
					break;
				elif ch == 'O':
					Ocnt+=1;
				elif ch == 'X':
					Xcnt+=1;		
				j+=1;
				
			if j==4:
				if Ocnt==0:
					winner='X';
					break;
				elif Xcnt==0:
					winner='O';
					break;

	if not winner:
		# check diagonals
			j=0;
			Ocnt=0;
			Xcnt=0;
			while (Ocnt==0 or Xcnt==0) and j<4:
				ch = board[j][j];
				if ch == '.':
					gameOver=0;
					break;
				elif ch == 'O':
					Ocnt+=1;
				elif ch == 'X':
					Xcnt+=1;		
				j+=1;
				
			if j==4:
				if Ocnt==0:
					winner='X';
				elif Xcnt==0:
					winner='O';

	if not winner:
		# check diagonals
			j=0;
			Ocnt=0;
			Xcnt=0;
			while (Ocnt==0 or Xcnt==0) and j<4:
				ch = board[3-j][j];
				if ch == '.':
					gameOver=0;
					break;
				elif ch == 'O':
					Ocnt+=1;
				elif ch == 'X':
					Xcnt+=1;		
				j+=1;
				
			if j==4:
				if Ocnt==0:
					winner='X';
				elif Xcnt==0:
					winner='O';												


	# output result
	if winner:			
		print('Case #', n+1, ': ', winner, ' won', sep='');
	elif gameOver:
		print('Case #', n+1, ': Draw', sep='');
	else:
		print('Case #', n+1, ': Game has not completed', sep='');					

	
	sys.stdin.readline(); # to cope with blank line

	
		