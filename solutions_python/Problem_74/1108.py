#!/usr/bin/env python

import sys, os

def main(*args):

	#~ I open the input file
	if len(sys.argv) > 1: 
		in_f = open(sys.argv[1], 'r')
	else: 
		in_f = open('_A.in', 'r')

	#~ I get the number of test cases and the input for each test case
	nbr_cases	= map(int,in_f.readline().strip())
	cases 		= [line.strip().split(" ") for line in in_f]
	in_f.close()

	#~ For each test case...
	for case in cases:
		secuence 	= case[1:]
		time		= 0
		turns 		= []
		orange_sec, orange_pos, orange_ptr	= [], 1, 0
		blue_sec, blue_pos, blue_ptr		= [], 1, 0
		
		#~ I get the secuence of buttons that each robot has to push
		for i in range(0,len(secuence),2):
			turns.append(secuence[i])
			if secuence[i] == 'O':
				orange_sec.append(int(secuence[i+1]))
			else:	
				blue_sec.append(int(secuence[i+1]))

		#~ I calculate the the minimum number of seconds required for the robots to push the given buttons
		while len(turns) != 0:
			time+=1
			pushed = False

			#~ If orange_robot has any buttons to push
			if 'O' in turns:

				#~ I check if it can push it, in which case it does
				if( (not pushed) and (turns[0] == 'O') and (orange_sec[orange_ptr] == orange_pos) ):
					pushed = True
					orange_ptr+=1
					turns.pop(0)

				#~ If not, I move it toward the next button it has to push or make it stay in the current position
				elif orange_sec[orange_ptr] > orange_pos:
					orange_pos+=1
				elif orange_sec[orange_ptr] < orange_pos:
					orange_pos-=1
				else:
					pass

			#~ If orange_robot has any buttons to push
			if 'B' in turns:

				#~ I check if it can push it, in which case it does
				if ( (not pushed) and (turns[0] == "B") and (blue_sec[blue_ptr] == blue_pos) ):
					pushed = True
					blue_ptr+=1
					turns.pop(0)

				#~ If not, I move it toward the next button it has to push or make it stay in the current position
				elif blue_sec[blue_ptr] > blue_pos:
					blue_pos+=1
				elif blue_sec[blue_ptr] < blue_pos:
					blue_pos-=1
				else:
					pass

		#~ I write down the answer in the output file
		print "Case #%d: %d" %(cases.index(case)+1,time)
	return 0


#this calls the 'main' function when this script is executed
if __name__ == '__main__': main(sys.argv)
