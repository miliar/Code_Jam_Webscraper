import sys
import operator
import string
import math

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
		LN.append(float(Str))
	return LN

#MAIN FUNCTION
T = input()
for X in range(1,T+1):
	D = input()
	P = InputLine()
	Porig = P[:]
	worstY = max(P)
	Y = max(P)
	tempY = Y
	Wait = [0] * len (P)
	WaitTot = 0
	while WaitTot < worstY:
		Plarge = max(P)
		iPl = P.index(Plarge)
		Wait[iPl] = Wait[iPl] + 1
		WaitTot = WaitTot + 1
		Pnew = math.ceil (Porig[iPl] / (Wait[iPl]+1))
		P[iPl] = Pnew
		tempY = max(P) + WaitTot
		if Y > tempY:
			Y = tempY
		
	Str = "Case #" + str(X) + ":"
	print Str, int(Y)
	sys.stdout.flush()
