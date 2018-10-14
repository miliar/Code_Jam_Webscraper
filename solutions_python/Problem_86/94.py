def checkFreq(x,y):
	if(x%y == 0 or y%x == 0):
		return True
	else:
		return False
		
T = int(raw_input())
for t in range(T):
	temp = raw_input().split(' ')
	N,L,H = int(temp[0]),int(temp[1]),int(temp[2])
	temp = raw_input().split(' ')
	note = []
	for i in range(N):
		note.append(int(temp[i]))
	haveFreq = False
	for i in range(L,H+1):
		check = True
		for j in note:
			if(checkFreq(j,i) == False):
				check = False
		if check:
			print "Case #" + str(t+1) + ": " + str(i)
			haveFreq = True
			break
	if(haveFreq == False):
		print "Case #" + str(t+1) + ": NO"
