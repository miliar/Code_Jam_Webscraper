def brattleshipSolution(R, C, W, tc, ofile):
	if W == C:
		if R == 1:
			ofile.write("Case #{0}: {1}\n".format(tc, W))
		else:
			ofile.write("Case #{0}: {1}\n".format(tc, R+W))	
	
	elif W == 1:
		ofile.write("Case #{0}: {1}\n".format(tc, R*C))
	
	else:
		if C%W == 0:
			chance = 1
		else:
			chance = 0
		overlaps = C/W
		oneRowSol = overlaps + W
		cases = R * oneRowSol
		sol = cases - ((R-1)*W)
		sol = sol - chance
		ofile.write("Case #{0}: {1}\n".format(tc, sol))

def Brattleship():
	file = open("/home/christian/Descargas/CodeJam/1C/Brattleship/A-small-attempt0.in", "r")
	ofile = open("/home/christian/Descargas/CodeJam/1C/Brattleship/solution.out", "w")
	test_cases = file.readline().strip()
	tc = 1
	for i in file:
		R, C, W = map(int, i.strip().split(" "))
		brattleshipSolution(R, C, W, tc, ofile)
		tc += 1
	ofile.close()
