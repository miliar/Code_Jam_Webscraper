#!/usr/bin/python
import sys
def evaluate(case):
	s_max = int(case[0])
	s_levels = case[1]
	activated = int(s_levels[0])
	friends = 0
	for i in range(1, s_max+1):
#		print "Activated ", activated, "; i ", i
		if activated >= i:
			activated += int(s_levels[i])
		else:
			new_friends = i - activated
			friends += new_friends
			activated += new_friends + int(s_levels[i])

	return friends

cases = int(raw_input(''))
for i in range(1, cases+1):
	case = raw_input('').split(' ')
	friends = evaluate(case)
#	print "Case #", i,": ", friends
	sys.stdout.write('Case #' + str(i) + ': ' + str(friends) + "\n")
