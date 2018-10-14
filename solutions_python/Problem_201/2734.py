def getGapToLeft(stallState, pos):
	gap = 0
	pos = pos-1
	while True:
		if (stallState[pos]):
			return gap;
		else:
			gap = gap + 1
			pos = pos + 1

def getGapToRight(stallState, pos):
	gap = 0
	pos = pos+1
	while True:
		if (stallState[pos]):
			return gap;
		else:
			gap = gap + 1
			pos = pos + 1

def solve(numStalls, numPeople):
	state = [False for x in range(numStalls)]
	state[0] = True;
	state[numStalls-1] = True;

	#print(state)

	for i in range(numPeople):
		#print(i, 'person is searching')
		#init alg values
		CurrentChoice = 0;
		#values for place 0 will always be the same, excpet gap to right

		GapToLeft = -1
		GapToRight = getGapToRight(state, 0)

		#print("found right")

		MaxMinOfLeftAndRight = GapToLeft
		MaxMaxOfLeftAndRight = max(-1, GapToRight)


		for scan in range(1, numStalls-1): #dont try the first or last stalls
			#print("curBest:", CurrentChoice, "scanning at", scan, end="")
			if (not state[scan]): #not occupied
				GapToLeft = GapToLeft+1 #find the values for this scan based on prev
				GapToRight = GapToRight-1

				#print("\tLeft:", GapToLeft, "Right:", GapToRight,)

				minLeftRight = min(GapToLeft,GapToRight)
				maxLeftRight = max(GapToLeft,GapToRight)

				if (minLeftRight > MaxMinOfLeftAndRight):
					#keep track of our best choice
					CurrentChoice = scan
					MaxMinOfLeftAndRight = minLeftRight
					MaxMaxOfLeftAndRight = maxLeftRight
				
				elif (minLeftRight == MaxMinOfLeftAndRight and maxLeftRight > MaxMaxOfLeftAndRight):
					CurrentChoice = scan
					MaxMinOfLeftAndRight = minLeftRight
					MaxMaxOfLeftAndRight = maxLeftRight
				
				else:
					continue;
			

			else:
				#print("\toccupied")
				GapToLeft = -1;
				GapToRight = getGapToRight(state,scan)

		#now we've found the leftmost best choice, so we fill it
		state[CurrentChoice] = True
	#print(state)
	return (MaxMaxOfLeftAndRight, MaxMinOfLeftAndRight)












#while True:
#	inp = [int(x) for x in input().split(',')]
#	print(solve(inp[0]+2,inp[1]))




with open('input', 'r') as f:
	read_data = f.readlines()

num = int(read_data[0])

with open('output', 'w+') as f:
	for i in range (num):
		args = [int(x) for x in (read_data[i+1]).split(" ")]

		output = solve(args[0]+2, args[1])

		f.write("Case #" + str(i+1) + ": " + str(output[0]) + " " + str(output[1]) + "\n")
