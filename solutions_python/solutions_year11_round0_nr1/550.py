#!/usr/bin/python
import sys

input = sys.argv[1]
#output = sys.argv[2]

input = open(input).read().strip().split("\n")

cases = int(input[0].strip())

result = ""
for i in range(0,cases):
	item = input[i+1].strip().split(" ")[1:]
	opos = 1
	bpos = 1
	actions = []
	for k in range(0,len(item)/2):
		actions.append((item[2*k],int(item[2*k+1])))
		
	if actions[0][0] == "O":
		initTime = abs(actions[0][1] - opos) + 1
		prev = "O"
		opos = actions[0][1]
	else:
		initTime = abs(actions[0][1] - bpos) + 1
		prev = "B"
		bpos = actions[0][1]
	totalTime = initTime
	for j in range(1,len(actions)):
		action = actions[j]
		if action[0] == "O":
			steps = abs(action[1] - opos)
			if prev == "O":
				totalTime += steps + 1
				initTime += steps + 1
			else:
				extra = steps-initTime
				if extra < 0:
					extra = 0
				totalTime += (extra) + 1
				initTime = (extra) + 1
			opos = action[1]
			prev = "O"
		else:
			steps = abs(action[1] - bpos)
			if prev == "B":
				totalTime += steps + 1
				initTime += steps + 1
			else:
				extra = steps-initTime
				if extra < 0:
					extra = 0
				totalTime += (extra) + 1
				initTime = (extra) + 1
			bpos = action[1]
			prev = "B"
	print "Case #"+str(i+1)+": " + str(totalTime)
#output = open(output,"w")
#output.write(result)
#output.close()
