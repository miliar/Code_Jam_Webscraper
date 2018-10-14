import sys

def checkproblem(problem):
	maxheight = max([max(y) for y in problem])
	
	for height in range(1, maxheight + 1):
		subproblem = [map(lambda x : x <= height, y) for y in problem]
		subproblem_trans = zip(*subproblem)
		
		# For each field ...
		for y in range(0, len(subproblem)):
			for x in range(0, len(subproblem[y])):
				# whose height is <= the current height:
				if subproblem[y][x]:
					# Check if the field lies in a row or a column where all
					# field heights are <= the current height
					if not all(subproblem[y]) and not all(subproblem_trans[x]):
						return False
		
	return True

with open(sys.argv[1]) as f:
	content = f.readlines()
	problemcount = int(content[0])
	line = 1

	for i in range(0, problemcount):
		problemsize = map(int, content[line].split())
		problem = [map(int, content[j].split()) for j in range(line + 1, line + problemsize[0] + 1)]
		line = line + problemsize[0] + 1

		print("Case #" + str(i+1) + ": " + ("YES" if checkproblem(problem) else "NO"))