def result(words):
	reps = []
	for i in range(len(words)):
		reps.append(represent(words[i]))
	for i in range(1,len(reps)):
		if(not possiblepair(reps[0],reps[i])):
			return "Fegla Won"
	moves = 0
	sums=[]
	for i in range(1,len(reps[0]),2):
		sums.append((int)(reps[0][i]))
	for i in range(1,len(reps)):
		for j in range(1,len(reps[i]),2):
			sums[j/2]+=(int)(reps[i][j])
	medels=[]
	for i in range(0,len(sums)):
		medels.append(((sums[i])+len(reps)//2)//len(reps))
	for i in range(0,len(reps)):
		for j in range(1,len(reps[i]),2):
			moves+=abs(reps[i][j]-medels[(j/2)])
	return moves

def moves(a,b):
	return a

def possiblepair(st1, st2):
	if(len(st1)!=len(st2)):
		return False
	lengd = min(len(st1), len(st2))
	for r in range(0,lengd,2):
		if(st1[r]!=st2[r]):
			return False
	return True

def represent(st):
	place = []
	place.append(st[0])
	place.append(1)
	k=1
	j=1
	for i in range(1,len(st)):
		if(st[i-1]!=st[i]):
			place[k]=j
			place.append(st[i])
			place.append(1)
			j=1
			k+=2
		else:
			j+=1
			if(i+1==len(st)):
				place[k]=j
	return place
	
T = int(raw_input())
for t in range(T):
	N = int(raw_input())
	words = []
	for n in range(N):
		s = raw_input()
		words.append(s)	
	print "Case #" + str(t+1) + ":", result(words)	


		
