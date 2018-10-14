import sys, operator, string, bin3

def Find (Vek,Ele):
	for i in range (len(Vek)):
		if Vek[i] == Ele:
			return i
	return -1

def Find2 (Vek,Ele1,Ele2):
	for i in range (len(Vek)):
		if (Vek[i] == Ele1) | (Vek[i] == Ele2):
			return i
	return -1

def BuildTree (t):
	i = 0
	while t[i] != '(': i = i+1
	while t[i] not in '1234567890': i = i+1
	j = i
	while t[j] in '1234567890.': j = j+1
	Val = float (t[i:j])
	while t[j] not in 'qwertzuiopasdfghjklyxcvbnm)': j = j+1
	if t[j] == ')':
		return [Val, 'N', None, None]
	i = j
	while t[i] in 'qwertzuiopasdfghjklyxcvbnm': i = i+1
	F = t[j:i]

	while t[i] != '(': i = i+1
	j = i+1
	Cpar = 1
	while Cpar > 0:
		if t[j] == ')': Cpar = Cpar-1
		if t[j] == '(': Cpar = Cpar+1
		j = j+1
	Left = t[i:j]

	i = j
	while t[i] != '(': i = i+1
	j = i+1
	Cpar = 1
	while Cpar > 0:
		if t[j] == ')': Cpar = Cpar-1
		if t[j] == '(': Cpar = Cpar+1
		j = j+1
	Right = t[i:j]
	return [Val, F, BuildTree(Left), BuildTree(Right)]

def InputStrLine():
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
		LN.append(Str)
	if len(LN)>0:
		LNend = LN[-1]
		LN[-1] = LNend[:-1]
	return LN

#MAIN FUNCTION
T = input()
for X in range(1,T+1):
	Str = "Case #" + str(X) + ":"
	print Str
	L = input()
	Tree = ''
	for i in range(L):
		Branch = sys.stdin.readline()
		Tree = Tree + Branch
	Baum = BuildTree(Tree)

	A = input()
	Tier = [0]*A
	n = [0]*A
	Feat = [0]*A
	for i in range(A):
		InList = InputStrLine()
		Tier[i] = InList[0]
		n[i] = int(InList[1])
		Feat[i] = InList[2:n[i]+2]
		Feat[i] = InList[2:]

		p = 1
		p = p * Baum[0]
#		print "p =", p
		Point = Baum
#		print Point
		while (Point[1] != 'N'):
			if Point[1] in Feat[i]:
				Point = Point[2]
			else: Point = Point[3]
#			print Point
			p = p * Point[0]
#			print "p = ",p

		print p
	sys.stdout.flush()
