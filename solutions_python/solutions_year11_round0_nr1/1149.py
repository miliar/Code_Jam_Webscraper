#!/usr/bin/python

import sys
import string
import math

#robot class for keeping track of place and timesense last move
class robot:
	def __init__(self):
		self.place=1
		self.time_sense_move=0


#how far will the robot have to move
def move(robot,next_button):
	if robot.time_sense_move>=abs(robot.place-next_button):
		steps=0
	else:
		steps = abs(robot.place-next_button)-robot.time_sense_move
	robot.place = next_button
	robot.time_sense_move=0
	return abs(steps)

#do a single run
def do_one_case(cnum):
	M = sys.stdin.readline().split()
	nMoves=int(M[0])
	bot_order = []
	place_order = []
	total_steps=0
	robot_A = robot()
	robot_B = robot()
	for i in range(1,nMoves*2,2):
		bot_order.append(M[i])
		place_order.append(int(M[i+1]))
	for i in range(nMoves):
		if bot_order[i]=='O':
			steps = move(robot_A,place_order[i])+1
			robot_B.time_sense_move+=steps
		if bot_order[i]=='B':
			steps = move(robot_B,place_order[i])+1
			robot_A.time_sense_move+=steps
		total_steps+=steps
	print "Case #%i: %i" % (cnum, total_steps)


def main():
	N = int(sys.stdin.readline().strip())
	for i in range(N):
		do_one_case(i+1)


if __name__ == "__main__":
	main()
