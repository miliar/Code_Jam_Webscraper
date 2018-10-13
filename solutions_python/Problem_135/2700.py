#!/usr/bin/python
# -*- coding:utf8 -*-

def testCase():

	found = False
	found_card = 0
	bad_magician = False
	mem = [0 for _ in xrange(4)]

	n1 = int(raw_input())
	for line in xrange(1,5):
		if line==n1:
			mem = map(int,raw_input().split(' '))
		else:
			raw_input()

	n2 = int(raw_input())
	for line in xrange(1,5):
		if line==n2:
			for card in map(int,raw_input().split(' ')):
				if card in mem:
					if found:
						bad_magician = True
					found = True
					found_card = card
		else:
			raw_input()

	if bad_magician:
		return 'Bad magician!'
	elif found:
		return found_card
	else:
		return 'Volunteer cheated!'


T = int(raw_input())
for i in xrange(1,T+1):
	print('Case #%d: %s'%(i,str(testCase())))
