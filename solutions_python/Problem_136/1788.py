#!/usr/bin/python


def main():
	
	fin = open("./data.in", "r")
	fout = open("./Cookie_Jam.txt", "w")

	firstline = 0

	for line in fin:
		if firstline != 0:
			line = line.split()
			
			cost_of_farm = float(line[0])
			addedrate  = float(line[1])
			goal = float(line[2])
			
			seconds = Calculate(cost_of_farm, addedrate, goal)
			fout.write("Case #" + str(firstline) + ": %.7f" % seconds + "\n")
			
		firstline+= 1

def Calculate(cost, addedrate, goal):
	rate = 2
	time = goal / (rate)
	temptime = 0
	
	bruteforce = 0

	while ( True ):
		rate = 2	
		temptime = 0.0
		bruteforce += 1
 
		#if time come back and optimize for speed
		for x in range(0, bruteforce):
			temptime += cost / (rate)
			rate += addedrate

		temptime += goal / (rate)

		if temptime < time:
			time = temptime
		else:
			break
	return time

main()
