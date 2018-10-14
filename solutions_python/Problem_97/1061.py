#!/usr/bin/env python

import sys

def count_recycle_pair(Min , Max):
	length = len(Min)
	if length < 2:
		return 0	

	count = 0
	Dict = {}
	i_min = int(Min)
	i_max = int(Max)

	for i_now in range(i_min, i_max):
		if i_now in Dict:
			continue
		Dict[i_now] = 1
		s_now = str(i_now)
		s_pair = s_now
		local_count = 0
		for i in range(0, length-1):
			s_pair = s_pair[1:length]+s_pair[0]			
			i_pair = int(s_pair)
			Dict[i_pair] = 1
			if i_pair != i_now and i_pair <= i_max and i_pair >= i_min:
				local_count+=1
				#print local_count, " : ", i_now ," " ,i_pair
		if local_count == 1:
			count+=1
		elif local_count ==2:
			count+=3
		elif local_count ==3:
			count+=6

	return count


# input and output
T = int( raw_input() )

for i in range(0, T):
	S = raw_input().split(" ")
	if len(S) !=2:
		print "error input : "+S
	A = S[0]
	B = S[1]

	print "Case #"+`i+1`+": "+ `count_recycle_pair(A, B)`

