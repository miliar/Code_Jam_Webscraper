T = int(raw_input())

for i in range(T):
	line = raw_input()
	S, string = line.split(' ', 2)
	S = int(S)
	friends = 0
	standingOvation = 0
	for index in range(S+1):
		if (standingOvation >= index):
			standingOvation += int(string[index])
		else:
			aux = index - standingOvation
			friends += aux
			standingOvation += aux
			standingOvation += int(string[index])

	print "Case #{}: {}".format(i+1, friends)

		
