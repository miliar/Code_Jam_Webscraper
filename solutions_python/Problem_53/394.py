import sys, operator, string

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

#MAIN FUNCTION
T = input()
for X in range(1,T+1):
	SA = InputLine()
	D = SA[0]
	E = SA[1]
	R = E & (2**D-1)
	if R == 2**D-1:
		Str = "Case #" + str(X) + ": ON"
	else:
		Str = "Case #" + str(X) + ": OFF"
	print Str
	sys.stdout.flush()
