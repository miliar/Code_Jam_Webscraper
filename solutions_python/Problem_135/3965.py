#!/usr/bin/python
import fileinput
#import time

line_number = 0
#f = 'sample-input.txt'
f = 'A-small-attempt0.in'
#f = 'A-large.in'

_f = open(f, 'r')

T = int(_f.readline().strip())

for t in xrange(T):
	_first_answer = int(_f.readline().strip())
	
	for c in xrange(4):
		_current_line = _f.readline()
		if (c+1 == _first_answer):
			_first_set = set(_current_line.strip().split(" "))
	
	#first set obtained
	_second_answer = int(_f.readline().strip())

	for c in xrange(4):
		_current_line = _f.readline()
		if (c+1 == _second_answer):
			_second_set = set(_current_line.strip().split(" "))
	
	_intersection = _first_set & _second_set
	if (len(_intersection) == 1):
		print "Case #"+str(t+1)+": "+_intersection.pop()
	elif (len(_intersection) > 1):
		print "Case #"+str(t+1)+": Bad magician!"
	else:
		print "Case #"+str(t+1)+": Volunteer cheated!"

