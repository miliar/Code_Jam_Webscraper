#!/usr/bin/env python

import sys

def count_pass(in_list):
	pass_man = 0
	man = int(in_list[0])
	special = int(in_list[1])
	threshold = int(in_list[2])
	score = []

	if threshold == 0:
		return man

	for i in range(man):
		score.append( int(in_list[i+3]) )
	score.sort()
	score.reverse()
	#decreasing

	must_pass_score = threshold*3 - 3
	may_pass_score = must_pass_score - 2	
	if may_pass_score < 1:
		may_pass_score = 1

	may_pass_count = 0

	for i in range(man):
		if score[i] > must_pass_score :
			pass_man +=1
		elif score[i] > may_pass_score :
			may_pass_count +=1

	if may_pass_count > special:
		pass_man += special
	else:
		pass_man += may_pass_count 

	return pass_man

T = int( raw_input() )

for i in range(0, T):
	in_list = raw_input().split(" ")
	pass_man = count_pass(in_list)
	print "Case #"+`i+1`+": "+`pass_man`


