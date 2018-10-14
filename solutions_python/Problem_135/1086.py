#!/usr/bin/python
import sys

def eval():
	a = [0 for x in range(0,16)]
	row = int(sys.stdin.readline())
	for j in range(1,5):
		line = sys.stdin.readline()
		cards = [int(k) for k in line.split()]
		if (j == row):
			val = 1
		else:
			val = 0
		for card in cards:
			a[card - 1] = val
	row = int(sys.stdin.readline())
	for j in range(1,5):
		cards = [int(k) for k in sys.stdin.readline().split()]
		if (j != row):
			for card in cards:
				a[card-1]=0
	p = [i for i in range(0,16) if a[i]==1]
	if (len(p) == 1):
		return str(p[0]+1)
	if (len(p) == 0):
		return 'Volunteer cheated!'
	return 'Bad magician!'

line = sys.stdin.readline()
cases = int(line)
for i in range(1,cases+1):
	print 'Case #' + str(i) + ': ' + eval()
