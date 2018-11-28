def solveA():
	fileIn = open("in.txt", "r")
	lines = [line.strip() for line in fileIn]
	fileIn.close()
	
	fileOut = open("out.txt", "w")
	
	
	T = int(lines[0])
	c = 0
	i = 1
	while c < T:
		chosen1 = int(lines[i])
		i += 1
		board1 = [line.split(" ") for line in lines[i:i+4]]
		i+=4
		chosen2 = int(lines[i])
		i += 1
		board2 = [line.split(" ") for line in lines[i:i+4]]
		i += 4
		c += 1
		result = "Case #%i: %s\n" % (c, solve(chosen1, board1, chosen2, board2))
		print result
		fileOut.write(result)
	
	fileOut.close()
		
def solve(chosen1, board1, chosen2, board2):
	possible = set(board1[chosen1-1]) & set(board2[chosen2-1])
	if len(possible) == 0:
		return "Volunteer cheated!"
	elif len(possible) == 1:
		return possible.pop()
	else:
		return "Bad magician!"
		
solveA()