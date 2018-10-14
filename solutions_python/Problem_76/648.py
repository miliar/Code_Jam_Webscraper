import string
M = int(input())
for c in range(1, M+1):
	N = int(input())
	L = [int(x) for x in str.split(raw_input())]
	L.sort()
	X = L[0]
	Y = 0
	Z = 0
	for i in range(1, N):
		Y = Y ^ L[i]
		Z = Z + L[i]
	if X == Y:
		print "Case #" + str(c) + ": " + str(Z)
	else:
		print "Case #" + str(c) + ": NO"
