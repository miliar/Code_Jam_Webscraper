#!/usr/bin/env python
from sys import *

def solve(lines):
	row1 = int(lines[0])
	board1 = lines[1:5]
	row2 = int(lines[5])
	board2 = lines[6:]
	
	cards = []
	
	for x in (board1[row1 - 1]).split(" "):
		for y in (board2[row2 - 1].split(" ")):
			if x == y: cards.append(x)
	
	if len(cards) == 0:
		return 'Volunteer cheated!'
	elif len(cards) == 1:
		return str(cards[0])
	else:
		return 'Bad magician!'
			

def read(counter):
	return [stdin.readline().strip("\n") for x in range(counter)]

def main():
	counter = int(stdin.readline())
	for x in range(counter):
		print("Case #" + str(x + 1) + ": " + str(solve(read(1 + 4 + 1 + 4))))

if __name__ == "__main__":
	main()
