import sys, math

def main(argv):
	input_file = open(argv[1], 'r')
	output_file = open(argv[2], 'w')
	lines = [line.rstrip('\n') for line in input_file]
	for x in range(1, len(lines)):
		stall = []
		stall.append ([1, int((lines[x].split(' '))[0])])
		people = int((lines[x].split(' '))[1])
		for y in range(0, people):
			index = 0
			ranged = -1
			for z in range(0, len(stall)):
				if (stall[z][1]-stall[z][0]) > ranged:
					ranged = stall[z][1]-stall[z][0]
					index = z
			place = math.floor((stall[index][1] + stall[index][0])/2)
			if stall[index][0] == place and stall[index][1] != place:
				stall.append([place + 1, stall[index][1]])
			elif stall[index][1] == place and stall[index][0] != place:
				stall.append([stall[index][0], place - 1])
			elif stall[index][0] == stall[index][1]:
				stall.append([-1,-1])
			else :
				stall.append([place + 1, stall[index][1]])
				stall.append([stall[index][0], place - 1])
			if y == people-1:
				r = stall[index][1] - place
				l = place - stall[index][0]
				output_file.write("Case #" + str(x) + ": " + str(max(l,r)) + " " + str(min(l,r)) + "\n")
			del(stall[index])

	input_file.close()
	output_file.close()

main(sys.argv)