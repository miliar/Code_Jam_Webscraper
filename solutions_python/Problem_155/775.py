import sys, operator, string

def Find (Vek,Ele):
	for i in range (len(Vek)):
		if Vek[i] == Ele:
			return i
	return -1

def Insert (Wort, n, s):
	if n not in Wort:
		Wort[n] = s

def InputLineA():
	StrLine = sys.stdin.readline()
	iSpace = StrLine.index(' ')
	Smax = int(StrLine[:iSpace])

	L = list(StrLine[iSpace+1:iSpace+Smax+2])
	LN = [int(x) for x in L]
	return LN

def CumuSum (List):
	CS = List[:]
	for i in range (len (List) - 1):
		CS [i+1] = CS [i] + List [i+1]
	return CS

#MAIN FUNCTION
T = input()
for X in range(1,T+1):
	NumStr = InputLineA()
	PSum = CumuSum (NumStr)
	Result = PSum[:]
	for (i, x) in enumerate (PSum):
		Result[i] = x - (i+1)
	m = min(Result)
	if m >= 0:
		Y = 0
	else:
		Y = -m

	Str = "Case #" + str(X) + ":"
	print Str, Y
	sys.stdout.flush()
