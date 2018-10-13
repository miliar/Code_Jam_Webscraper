import sys, operator, string


def Find (Vek,Ele):
	for i in range (len(Vek)):
		if Vek[i] == Ele:
			return i
	return -1

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
			if (j < i) and (A > EL[j]):
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
	N = input()
	ABold = []
	for i in range(N):
		ABold.append (InputLine())
	AB = SortNumList (ABold)
	
	Y = 0
	for j in range(1,N):
		ab = AB[j]
		bj = ab[1]
		for i in range(j):
			ab = AB[i]
			if bj < ab[1]: Y = Y + 1
			
	Str = "Case #" + str(XX) + ":"
	print Str, Y
	sys.stdout.flush()
