

def add(t,turn):
	r = []
	r.extend(t)
	r[1] = (turn+t[1])%60
	r[0] += (turn+t[1])/60
	return r

T = int(raw_input())
for x in range(0,T):
	turn = int(raw_input())
	s = raw_input().split()
	NA,NB = int(s[0]), int(s[1])
	listA,listB = [],[]
	
	for i in range(0,NA):
		s = raw_input().split()
		t = s[0].strip().split(":")
		f = [int(t[0]),int(t[1])]
		t = s[1].strip().split(":")		
		f2 = add([int(t[0]),int(t[1])], turn)
		listA.append([f,f2])
	listA.sort()
	
	for i in range(0,NB):
		s = raw_input().split()
		t = s[0].strip().split(":")
		f = [int(t[0]),int(t[1])]
		t = s[1].strip().split(":")		
		f2 = add([int(t[0]),int(t[1])], turn)
		listB.append([f,f2])
	listB.sort()
	
	i,j=0,0
	A,B = len(listA),len(listB)
	tA = []
	tA.extend(listA)
	tB = []
	tB.extend(listB)
	for i in range(0,len(listA)):
		get = -1
		for j in range(0,len(tB)):
			if (listA[i][1] <= tB[j][0]):
				get = j
				break
		if get!=-1:
			del tB[j]
	B = len(tB)
	for i in range(0,len(listB)):
		get = -1
		for j in range(0,len(tA)):
			if (listB[i][1] <= tA[j][0]):
				get = j
				break
		if get!=-1:
			del tA[j]
	A = len(tA)
	print "Case #%d: %d %d" % (x+1, A, B)
			
		
		
