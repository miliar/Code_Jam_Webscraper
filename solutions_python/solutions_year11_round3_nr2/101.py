def checkFreq(x,y):
	if(x%y == 0 or y%x == 0):
		return True
	else:
		return False
		
T = int(raw_input())
for t in range(T):
	temp = raw_input().split(' ')
	L,ti,N,C = int(temp[0]),int(temp[1]),int(temp[2]),int(temp[3])
	distan = []
	for i in range(C):
		distan.append(int(temp[i+4]))
	star = []
	j = 0
	sumTime = 0
	for i in range(N+1):
		star.append([distan[j],sumTime])
		sumTime += distan[j]*2
		j = (j+1)%C
	if(L == 1):
		maxDec = 0
		for i in range(N):
			if(ti < star[i+1][1]):
				if(ti > star[i][1]):
					timeDec = (star[i+1][1] - ti)/2
				else:
					timeDec = star[i][0]
				#print timeDec
				if(timeDec > maxDec):
					maxDec = timeDec
		print "Case #" + str(t+1) + ": " + str(star[N][1] - maxDec)
	elif(L == 2):
		maxDec = 0
		for i in range(N):
			if(ti < star[i+1][1]):
				if(ti > star[i][1]):
					timeDec = (star[i+1][1] - ti)/2
				else:
					timeDec = star[i][0]
				j = i+1
				while(j < N):
					timeDec2 = star[j][0]
					if(timeDec2 + timeDec > maxDec):
						maxDec = timeDec2 + timeDec
					j += 1
		print "Case #" + str(t+1) + ": " + str(star[N][1] - maxDec)
					#if(t < star[j+1][1] - timeDec)
	else:
		print "Case #" + str(t+1) + ": " + str(star[N][1])
			
