import sys, operator

def Find (Vek,Ele):
	for i in range (len(Vek)):
		if Vek[i] == Ele:
			return i
	return -1

def FindAll (Vek,Ele):
	R = []
	for i in range (len(Vek)):
		if Vek[i] == Ele:
			R.append(i)
	return R

def InputLine():
	StrLine = sys.stdin.readline()
	L = [StrLine]
	n = 1
	i = Find (StrLine,' ')
	while i >= 0:
		L[n-1:] = [StrLine[:i], StrLine[i+1:]]
	StrLine = StrLine[i+1:]
	n = n+1
	i = Find (StrLine,' ')
	L[n-1:] = [StrLine[:i], StrLine[i+1:]]
	StrLine = StrLine[i+1:]
	n = n+1
	return L

def Function (b, a):
	F = FindAll (b, a[0])
	if len(a) == 1: return len(F)
	Tot = 0
	for i in F:
		Tot = Tot + Function (b[i+1:], a[1:])
		if Tot > 999: Tot = Tot%1000
	return Tot

#MAIN FUNCTION
T = input()
for X in range(1,T+1):
	Sentence = sys.stdin.readline()
	N = Function (Sentence,"welcome to code jam")

	Y = str(N)
	Str = "Case #" + str(X) + ":"
	print Str, Y.zfill(4)
	sys.stdout.flush()
