import sys, operator, string

def PurgeZeros (TMZ):
	L = len(TMZ)
	i = 0
	while (i < L) and (TMZ[i] == 0):
		i = i + 1
	return TMZ[i:]
	
def Minus (A,B):	# A - B as if they were decimal numbers
	Base = 10
	Lab = len(A)
	if Lab != len(B): return [-1]
	C = []
	r = 0
	for i in range (1,Lab+1):
		C = [A[-i] - B[-i] - r] + C
		if C[0] < 0:
			C[0] = C[0] + Base
			r = 1
		else: r = 0
	if r > 0: return [-1]
	return PurgeZeros(C)

def Find (Vek,Ele):
	for i in range (len(Vek)):
		if Vek[i] == Ele:
			return i
	return -1

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
			if A > EL[j]:
				j = j + p
				if j > i: j = i
			else:
				j = j - p
				if j < 0: j = 0
		EL = EL[:j] + [A] + EL[j:]
	return EL

#MAIN FUNCTION
C = input()
for XX in range(1,C+1):
	NKBT = InputLine()
	N = NKBT[0]
	K = NKBT[1]
	B = NKBT[2]
	T = NKBT[3]
	Y = 0
	X = InputLine()
	V = InputLine()
	
	bX = []
	vT = []
	iList = []
	iN = 0
	for i in range(N):
		bX.append(B-X[i])
		vT.append(V[i]*T)
		if bX[i] <= vT[i]:
			iN = iN + 1
			iList.append(i)
	
	Str = "Case #" + str(XX) + ":"
	if iN < K: print Str, "IMPOSSIBLE"
	else:
		iListK = iList[-K:]
		SumReal = sum(iListK)
		SumIdeal = K*N - K*(K+1)/2
		Y = SumIdeal - SumReal
		print Str, Y
	sys.stdout.flush()
