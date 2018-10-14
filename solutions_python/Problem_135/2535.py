#!/usr/bin/python

T = int(raw_input())

for t in xrange(T):
	
	cards = []
	
	# read first answer:
	answer = int(raw_input())
	
	# read the cards:
	for r in xrange(4):
		cards += [map(int, raw_input().split())]
	
	# first row
	r1 = cards[answer-1]
	
	# read second answer:
	answer = int(raw_input())
	
	# re-read the cards:
	cards = []
	for r in xrange(4):
		cards += [map(int, raw_input().split())]
	
	# second row
	r2 = cards[answer-1]
	
	numbers = [x for x in r1 if x in r2]
	
	if len(numbers) == 0:
		print "Case #%d: Volunteer cheated!" % (t+1)
	elif len(numbers) == 1:
		print "Case #%d: %d" % (t+1, numbers[0])
	elif len(numbers) > 1:
		print "Case #%d: Bad magician!" % (t+1)