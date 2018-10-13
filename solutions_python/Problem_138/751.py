import sys

fin  = open("D-large.in", "r")
fout = open("output_4s.txt", "w")

def getWin(N, K):
	win = 0
	j = 0
	for i in xrange(len(N)):
		if N[i] > K[j]:
			win += 1
		else:
			j += 1
	return win	

def getDWin(N, K):
	win = 0
	for i in xrange(len(N)):
		if N[i] > K[i]:
			win += 1
	return win	


case = int(fin.readline().strip())
for c in xrange(case):
	nBlock = int(fin.readline().strip())
	N = map(float, fin.readline().strip().split())
	K = map(float, fin.readline().strip().split())
	N.sort(reverse=True)
	K.sort(reverse=True)
	win = getWin(N, K)
	winList = list()
	winList.append(getDWin(N, K))
	for i in xrange(nBlock):
		if N[-1] > K[0]:
			break
		N.pop(-1)
		K.pop(0)
		tmpWin = getDWin(N, K)
		winList.append(tmpWin)
	dWin = max(winList)


	fout.write("Case #" + str(c + 1) + ": " + str(dWin) + " " + str(win) + "\n")

fin.close()
fout.close()