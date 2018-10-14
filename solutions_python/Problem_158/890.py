import math
fin = open("in.txt","r")


N = int(fin.readline())


f = open( "out.txt","w")


for T in range(N):
	(X,R,C) = map(int, fin.readline().split())
	winner = ""
	diag = X/2
	if (R*C) % X != 0:
		winner = "RICHARD"
	elif (diag >= R or diag >=C) and (diag != 1):
		winner = "RICHARD"
	elif X>2 and (R == 1 or C== 1):
		winner = "RICHARD"
	else:
		winner = "GABRIEL"
	f.write("Case #{}: {}\n".format(T+1,winner))


f.close()

fin.close()