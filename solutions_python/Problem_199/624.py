t = int(input())
for i in range (1,t+1):
	pan = input()
	pan = pan.split()
	l = int(pan[1])
	pan = list(pan[0])
	nflip = 0
	for j in range(0,len(pan)-l+1):
		if(pan[j]=='-'):
			nflip = nflip+1
			for k in range(0,l):
				if(pan[j+k]=='-'):
					pan[j+k]='+'
				else:
					pan[j+k]='-'
	for j in range(len(pan)-1,len(pan)-l,-1):
		foundmin = pan[j]=='-'
		if foundmin: break
	if not foundmin:
		print("Case #"+str(i)+": "+str(nflip),end='\n')
	else:
		print("Case #"+str(i)+": IMPOSSIBLE",end='\n')