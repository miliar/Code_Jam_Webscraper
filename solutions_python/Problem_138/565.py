def War(M,A,B):
	winN = 0
	for i in range(0,M):
		win = True
		for j in range(0,len(B)):
			if A[0]<B[j]:
				del B[j]
				win = False
				break
		if win:
			del(B[0])
			winN += 1
		del(A[0])
	return winN
def DWar(M,A,B):
	while True:
		allWin = True
		for x,y in zip(A,B):
			if x<y:
				allWin = False
				break
		if allWin:
			return len(A)
		else:
			del(A[0])
			del(B[len(B)-1])



my_file = open('Input.txt',"r")
my_file2 = open('Output.txt', "w")
case = int(my_file.readline())
for i in range(1,case+1):
	M = int(my_file.readline())
	A = my_file.readline().split()
	A = sorted([float(x) for x in A])
	B = my_file.readline().split()
	B = sorted([float(x) for x in B])
	AA = A[:]
	BB = B[:]
	dwin = DWar(M,AA,BB)
	win = War(M,A,B)
	my_file2.write("Case #"+str(i)+": "+str(dwin)+" "+str(win)+"\n")
my_file.close()
my_file2.close()
