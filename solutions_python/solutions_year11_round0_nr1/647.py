inp = file("input")
T = inp.readline()
out = file("output", "w")
case = 0

for line in inp.readlines():
	case += 1
	line = line.split()
	N = int(line[0])
	O = []
	B = []
	Seq = []
	pO = 1
	pB = 1
	for j in xrange(1,2*N+1,2):
		Seq.append(line[j])
		if line[j] == "O":
			O.append(int(line[j+1]))
		else:
			B.append(int(line[j+1]))
	time = 0
	r = 0
	while r < len(Seq):
		if Seq[r] == "O":
			if pO == O[0]:
				time += 1
				O.pop(0)
				r += 1
				if B != []:
					if pB != B[0]:
						pB += (abs(pB - B[0]))/(B[0] - pB)
			else:
				if B != []:
					if abs(O[0] - pO) < abs(B[0] - pB):
						pB += (abs(pB - B[0]))/(B[0] - pB)*(abs(O[0] - pO))
					else:
						pB = B[0]
				time += abs(O[0] - pO)
				pO = O[0]
		else:
			if pB == B[0]:
				time += 1
				B.pop(0)
				r += 1
				if O != []:
					if pO != O[0]:
						pO += (abs(pO - O[0]))/(O[0] - pO)
			else:
				if O != []:
					if abs(B[0] - pB) < abs(O[0] - pO):
						pO += (abs(pO - O[0]))/(O[0] - pO)*(abs(B[0] - pB))
					else:
						pO = O[0]
				time += abs(B[0] - pB)
				pB = B[0]
	out.write("Case #" + str(case) + ": " + str(time) + "\n")
