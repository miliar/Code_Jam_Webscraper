#! /usr/bin/env python
import sys

def evaluate_situation(board):
	empty = False
	for x in range(4):
		result = eval_line(board[x])
		if result == 'X':
			print 'X won'
			return 1
		elif result == 'O':
			print 'O won'
			return 1
		elif result == 'E':
			empty = True
	
	if empty:
		return 0
	else:
		return -1

def eval_line(line):
	X = 0
	O = 0
	T = 0
	E = 0
	for i in range(4):
		if line[i] == 'X':
			X += 1
		elif line[i] == 'O':
		   	O += 1
		elif line[i] == 'T':
			T += 1
		elif line[i] == '.':
			E += 1
	if E > 0:
		return 'E'
	elif X > O and X + T == 4:
		return 'X'
	elif X < O and O + T == 4:
		return 'O'

def evaluate_line(line):
	result = eval_line(line)
	if result == 'X':
        	print 'X won'
                return True
        elif result == 'O':
                print 'O won'
                return True
        else:
        	return False
	

def process_input():
	sets = int(sys.stdin.readline())
	for i in range(sets):
		line = [' ' for x in range(4)]
		board = [[' ' for x in xrange(4)] for x in xrange(4)] 
		sys.stdout.write("Case #"+str(i+1)+": ")
		for j in range(4):
			board[j] = list(sys.stdin.readline().strip())
		sys.stdin.readline()
		result1 = evaluate_situation(board)
		if not (result1 > 0):
			result2 = evaluate_situation(zip(*board))
		else:
			result2 = result1
		empty = result1 == 0
		if not (result1 > 0 or result2 > 0):
			for j in range(4):
				line[j] = board[j][j]
			if not evaluate_line(line):
		                for j in range(4):
	        	                line[j] = board[3-j][j]
				if not evaluate_line(line):
					if empty:
						print 'Game has not completed'
					else:	
						print 'Draw'



process_input()
