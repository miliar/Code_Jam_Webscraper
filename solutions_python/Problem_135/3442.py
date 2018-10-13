#!/usr/bin/env python
cases = input()
case=0
while case < cases :
	case+=1;
	row1_index = input()
	row1 = []
	row2 = []
	count = 0;
	number = -1;
	for i in xrange(1,5):
		if i == row1_index:
			row1 = map(int,raw_input().split(" "))
		else:
			dev_null=raw_input()
	row2_index = input()
	for i in xrange(1,5):
		if i == row2_index:
			row2 = map(int,raw_input().split(" "))
		else:
			dev_null=raw_input()
	for x in row1:
		if x in row2:
			number = x;
			count+=1;
	if count == 0:
		print "Case #"+str(case)+": Volunteer cheated!"
	elif count == 1:
		print "Case #"+str(case)+": " + str(number)
	else:
		print "Case #"+str(case)+": Bad Magician!"


