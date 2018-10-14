#!/usr/bin/python
import sys

data = sys.stdin.readlines()
cases = int(data.pop(0))
case = 1

while (case <= cases):
	Oposition = 1 #current position of O and B
	Bposition = 1
	
	Oqueue = [] #queue of buttons to press
	Bqueue = []
	
	orderQueue = [] #who's turn it is to press
	
	sys.stdout.write("Case #%d: " % case)
	line = data.pop(0) #get the line
	words = line.split() #separate by spaces
	buttons_to_press = int(words.pop(0))
	
	for item in words: #put line in data structures
		if item == 'O' or item == 'B':
			orderQueue.append(item)
		else:
			if orderQueue[-1] == 'O':
				Oqueue.append(int(item))
			else:
				Bqueue.append(int(item))
	
	#len(orderQueue) should equal buttons_to_press	
	pressed = 0
	seconds = 0
	while (pressed < buttons_to_press):
		pushed = 0
		#Blue decision
		if len(Bqueue) > 0:
			if Bposition == Bqueue[0]: #at the right position
				if orderQueue[0] == 'B' and pushed == 0: #blue turn to push
					Bqueue.pop(0)
					orderQueue.pop(0)
					pressed += 1
					pushed += 1
			else: #not the right position
				target = Bqueue[0]
				if (target - Bposition) < 0:
					Bposition -= 1
				else:
					Bposition += 1

		#orange decision
		if len(Oqueue) > 0:
			if Oposition == Oqueue[0]: #at the right position
				if orderQueue[0] == 'O' and pushed == 0: #orange turn to push
					Oqueue.pop(0)
					orderQueue.pop(0)
					pressed += 1
					pushed += 1
			else: #not the right position
				target = Oqueue[0]
				if (target - Oposition) < 0:
					Oposition -= 1
				else:
					Oposition += 1
			
		seconds += 1
	
	sys.stdout.write("%d\n" % seconds)
	case += 1