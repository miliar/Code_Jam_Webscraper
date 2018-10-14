#!/usr/bin/env python
import sys
import re

Pos = { 'O' : 0, 'B' : 0}

def getNext(L, color, event):
	for i in range(event*2,len(L),2):
		if L[i] == color:
			return (i/2, int(L[i+1]))

def stepRobot(L, color, goal, event, dis):
	global Pos
	if goal == None:
		return 0
#	print "stepRobot", color, goal, event, Pos

	if Pos[color] > goal[1]:
		Pos[color]-=1
	elif Pos[color] < goal[1]:
		Pos[color]+=1
	else:
		if goal[0] == event and not dis:
			return 1
	return 0

    
def main():
	T = raw_input()
	for t in range(int(T)):
		L = raw_input().split()
		S = int(L[0])
		L = L[1:]
		if(t < 0):
			continue
		Pos['O'] = 0
		Pos['B'] = 0
		EVENT = 0
		ONext = getNext(L, 'O', EVENT)
		BNext = getNext(L, 'B', EVENT)

#		print L
		STEP = 0
		while EVENT < S:
			STEP+=1
			dis = False
			if stepRobot(L, 'O', ONext, EVENT, dis) == 1:
				EVENT +=1;
				ONext = getNext(L, 'O', EVENT)
				dis = True

			if stepRobot(L, 'B', BNext, EVENT, dis) == 1:
				EVENT +=1;
				BNext = getNext(L, 'B', EVENT)

		print "Case #"+str(t+1)+": " + str(STEP-1)

if __name__ == "__main__":
    main()
