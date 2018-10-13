from math import ceil

def xomino(X, R, C):
	A = R * C
	if (X==1) or (X==2 and A%2==0) or (X==3 and A in [6,9,12,15]):
		return "GABRIEL"
	if X==4 and ((A==16) or (R==3 and C==4) or (R==4 and C==3)):
		return "GABRIEL"
	return "RICHARD"



T = int(input())
for case in range(1, T+1):
	X,R,C = list(map(int, input().split()))
	print("Case #{0}: {1}".format(case, xomino(X,R,C)))