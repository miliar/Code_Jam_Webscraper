T = int(input())

for t in range(1, T + 1):
	N, R, O, Y, G, B, V = [int(s) for s in input().split(" ")]
	
	limit = N / 2
	possible = limit >= R and limit >= Y and limit >= B
	
	if (possible):
		solution = ""
		
		if (R >= Y and R >= B):
			solution += "R"
			R -= 1
		elif (Y >= R and Y >= B):
			solution += "Y"
			Y -= 1
		else:
			solution += "B"
			B -= 1
		
		
		while (R > 0 or Y > 0 or B > 0):
			if (solution[-1] == "R"):
				if (Y >= B):
					solution += "Y"
					Y -= 1
				else:
					solution += "B"
					B -= 1
			elif (solution[-1] == "Y"):
				if (R >= B):
					solution += "R"
					R -= 1
				else:
					solution += "B"
					B -= 1
			else:
				if (R >= Y):
					solution += "R"
					R -= 1
				else:
					solution += "Y"
					Y -= 1

		if (solution[0] == solution[-1]):
			aux = solution[-2]
			solution = solution[:-2] + solution[0]
			solution += aux
					
	print("Case #{}: {}".format(t, solution if possible else "IMPOSSIBLE"))