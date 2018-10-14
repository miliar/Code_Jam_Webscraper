def myStall(N, K):
	occupied = [0,N+1]
	for person in range(K):
		maxSpace = 0
		left = 0
		right = 0
		for i in range(1, len(occupied)):
			space = occupied[i] - occupied[i-1] - 1
			if space > maxSpace:
				maxSpace = space
				right = occupied[i]
				left = occupied[i-1]

		if (maxSpace%2 == 0):
			position = left + maxSpace/2

		else:
			position = left + maxSpace/2 + 1
		
		occupied.append(position)
		occupied.sort()

	L = position-left-1
	R = right-position-1

	return [L,R]

with open("C-small.out", 'w') as output:
	with open("C-small-1-attempt1.in", 'r') as input:
		input.readline()
		case = 1
		for line in input:
			data = line.strip().split(" ")
			N = int(data[0])
			K = int(data[1])
			result = myStall(N, K)	
			output.write("Case #" + str(case) + ": " + str(max(result)) + " " + str(min(result)) + "\n")
			case += 1