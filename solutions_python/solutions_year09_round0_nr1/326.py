import sys, operator

def Find (Vek,Ele):
	for i in range (len(Vek)):
		if Vek[i] == Ele:
			return i
	return -1

def InputLine():
	StrLine = sys.stdin.readline()
	L = [StrLine]
	LN = []
	i = Find (StrLine,' ')
	n = 1
	while i >= 0:
		L[n-1:] = [StrLine[:i], StrLine[i+1:]]
		StrLine = StrLine[i+1:]
		i = Find (StrLine,' ')
		n = n+1
	for Str in L:
		LN.append(int(Str))
	return LN

def Extract (w,L):
#	Lw = len(w)
	l = 0
	p = []
	while l<L:
#		print w, l, "of", L
		if w[0] == '(':
			f = Find (w,')')
			p.append (w[1:f])
			w = w[f+1:]
		else:
			p.append (w[0])
			w = w[1:]
		l = l+1
	return p

#MAIN FUNCTION
InList = InputLine()
L = InList[0]
D = InList[1]
N = InList[2]
Dict = []
Patterns = []
K = [0]*N
for W in range(D):
	Word = sys.stdin.readline()
	Dict.append(Word)
for Y in range(N):
	Word = sys.stdin.readline()
#	Patterns.append(Word)
	Pat = Extract(Word,L)

	for d in range(D):
		Match = True
		l = 0
		while (Match == True) & (l < L):
			Match = Dict[d][l] in Pat[l]
			l = l+1
		if Match == True:
			K[Y] = K[Y]+1

	Str = "Case #" + str(Y+1) + ":"
	print Str, K[Y]
	sys.stdout.flush()
