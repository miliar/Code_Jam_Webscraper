import sys

W = "welcome to code jam"

for i in range(int(sys.stdin.readline())):
	print "Case #%d:" % (i+1),
	S = sys.stdin.readline().rstrip()
	NN = []
	for x in range(len(W)):
		NN.append([0]*len(S))
		
	for x in range(len(W)):
		for y in range(x, len(S)):
			if W[x] == S[y]:
				if x == 0:
					NN[x][y] = (NN[x][y-1] + 1) % 1000
				else:
					NN[x][y] = (NN[x-1][y] + NN[x][y-1]) % 1000
			elif y>0:
				NN[x][y] = NN[x][y-1]
#	for x in range(len(W)):
#		print NN[x]
	print "%04d" % (NN[len(W)-1][len(S)-1] % 1000)
		