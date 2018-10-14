def makingintK(L):
	J=[]
	for i in range(0,len(L)):
		J.append(L[i]*1000000)
	J = map(int,J)
	return(J)

def makingintN(L):
	J=[]
	for i in range(0,len(L)):
		J.append(L[i]*1000000+1)
	J = map(int,J)
	return(J)

def SortandElim(L1,L2):
	S = sorted(L1 + L2)
	print(S)
	N = []
	for i in range(0,len(S)):
		N.append(S[i]%10)
	return(N)

def RegWar(L):
	extra = 0
	KWins = 0
	for i in range(0,len(L)):
		if L[i]==0:
			if extra > 0:
				KWins = KWins + 1
				extra = extra -1
		else:
			extra = extra + 1
	return(KWins)

def InputTaker(Filename):
	Input = open(Filename,"r")
	return(Input)

f = InputTaker("D-small-attempt0.in.txt")

file = open("NaomiandKenOutput.txt", "w")

a = int(f.readline())
for i in range(0,a):
	b = int(f.readline())
	NList = map(float,f.readline().split())
	KList = map(float,f.readline().split())
	D = RegWar(SortandElim(makingintN(KList),makingintK(NList)))
	R = RegWar(SortandElim(makingintN(NList),makingintK(KList)))
	print(NList)
	print(KList)
	file.write("Case #"+str(i+1)+": " + str(D) + " " + str(b-R) + "\n")

"S = SortandElim(makingintN(L1),makingintK(L2))"
"print(S)"

"print(RegWar(S))"