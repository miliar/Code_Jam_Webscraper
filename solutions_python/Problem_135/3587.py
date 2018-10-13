#!/usr/bin/python2.7
import sys

def compute(answer, cards):
	intersect = list(set(cards[0][answer[0]-1]) & set(cards[1][answer[1]-1]))
	if len(intersect) == 0:
		return "Volunteer cheated!"
	elif len(intersect) == 1:
		return intersect[0]
	else:
		return "Bad magician!"

lines = sys.stdin.read().splitlines()
num_cases = int(lines.pop(0))

for i in xrange(num_cases):
	answer = []
	cards = []
	answer.append(int(lines.pop(0)))
	cards.append([map(int, lines.pop(0).split()) for tmp in xrange(4)])
	answer.append(int(lines.pop(0)))
	cards.append([map(int, lines.pop(0).split()) for tmp in xrange(4)])
	print "Case #{0}: {1}".format(i+1, compute(answer,cards))

