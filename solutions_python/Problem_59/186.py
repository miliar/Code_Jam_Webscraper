import sys, operator, string


def Find (Vek,Ele):
	for i in range (len(Vek)):
		if Vek[i] == Ele:
			return i
	return -1

def FindIns (Vek,Ele):
	for i in range (len(Vek)):
		if Vek[i] > Ele:
			return i
	return len(Vek)

def Insert (Wort, n, s):
	if n not in Wort:
		Wort[n] = s

def InputLine():
	StrLine = sys.stdin.readline()
	L = [StrLine]
	LN = []
	n = 1
	i = Find (StrLine,' ')
	while i >= 0:
		L[n-1:] = [StrLine[:i], StrLine[i+1:]]
		StrLine = StrLine[i+1:]
		n = n+1
		i = Find (StrLine,' ')
	for Str in L:
		LN.append(int(Str))
	return LN

def InputPath():
	StrLine = sys.stdin.readline()[1:]
	if StrLine[-1] not in '1234567890qwertzuiopasdfghjklyxcvbnm':
		StrLine = StrLine[:-1]
	L = [StrLine]
	n = 1
	i = Find (StrLine,'/')
	while i >= 0:
		L[n-1:] = [StrLine[:i], StrLine[i+1:]]
		StrLine = StrLine[i+1:]
		n = n+1
		i = Find (StrLine,'/')
	return L

def SortNumList (Biglist):
	L = len(Biglist)
	if L == 0: return []
	EL = [Biglist[0]]
	for i in range(1,L):
		A = Biglist[i]
		j = i/2
		p = i/2+1
		while ((j>0)or(A>EL[0])) and ((j<i)or(A<EL[i-1])) and ((A<EL[j-1])or(A>EL[j])):
			if p>2: p = p/2+1
			else: p = 1
			if (j < i) and (A > EL[j]):
				j = j + p
				if j > i: j = i
			else:
				j = j - p
				if j < 0: j = 0
		EL = EL[:j] + [A] + EL[j:]
	return EL

def FinalPart (Where,What):
	La = len(What)
	Lb = len(Where)
	i = 0
	while (i < La) and (i < Lb) and (Where[i] == What[i]):
		i = i + 1
	return [i,What[i:]]

#MAIN FUNCTION
T = input()
for X in range(1,T+1):
	InList = InputLine()
	N = InList[0]
	M = InList[1]
	LN = []
#	LM = []
	Y = 0
	for n in range(N):
		A = InputPath()
		LN.append(A)
		
	LNnew = SortNumList(LN)
	for m in range(M):
		A = InputPath()
#		LM.append(A)
		pos = FindIns (LNnew,A)
		La = len(A)
		ToAdd = []
		if pos == 0: # no existing path
			Y = Y + La
			for i in range(La):
				ToAdd.append(A[:i+1])
			LNnew = ToAdd + LNnew
		else:
			B = LNnew[pos-1]
			CPQKM = FinalPart(B,A)
			CP = CPQKM[0]
			QKM = CPQKM[1]
			Lq = len(QKM)
			Y = Y + Lq
			for i in range(Lq):
				ToAdd.append(A[:CP+i+1])
			LNnew = LNnew[:pos] + ToAdd + LNnew[pos:]

	Str = "Case #" + str(X) + ":"
	print Str, Y
	sys.stdout.flush()
