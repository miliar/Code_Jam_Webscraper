def Rlistmult(L):
	J = list(L)
	K = []
	L = []
	m=1
	if len(J) == 1:
		K.append(J[0])
		L.append(1)
	else:
		for i in range(1,len(J)):
			if J[i]==J[i-1] and i != len(J)-1:
				m = m+1
			elif J[i]==J[i-1] and i == len(J)-1:
				K.append(J[i])
				m = m+1
				L.append(m)
			elif i != len(J)-1:
				K.append(J[i-1])
				L.append(m)
				m = 1
			else:
				K.append(J[i-1])
				L.append(m)
				K.append(J[i])
				L.append(1)
	return([K,L])

def Minmoves(Kk,Ll):
	wins = 0
	avesum = 0.
	moves = 0
	for i in range(1,len(Kk)):
		if Kk[i] != Kk[i-1]:
			wins = wins+1
	if wins == 0:
		for j in range(0,len(Ll[1])):
			for i in range(0,len(Kk)):
				avesum = avesum + float(Ll[i][j])

			ave = round(avesum/len(Kk))

			for i in range(0,len(Kk)):
				moves = int(moves + abs(Ll[i][j] - ave))
			avesum = 0
	else:
		moves = -1
	return(moves)

def InputTaker(Filename):
	Input = open(Filename,"r")
	return(Input)
		
f = InputTaker("A-small-attempt0.in.txt")

file = open("AOutput.txt","w")

a = int(f.readline())

for i in range(0,a):
	b = int(f.readline())
	Kk = []
	Ll = []
	for j in range(0,b):
		reader = str(f.readline().rstrip("\n"))
		print(reader)
		KL = Rlistmult(reader)
		Kk.append(KL[0])
		Ll.append(KL[1])
		print(Kk)
		print(Ll)
	moves = Minmoves(Kk,Ll)
	print(moves)
	if moves == -1:
		file.write("Case #"+str(i+1)+": Fegla Won \n")
	else:
		file.write("Case #"+str(i+1)+": " + str(moves) + "\n")

