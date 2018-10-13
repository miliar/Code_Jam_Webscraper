>>> def memo(f):
	cache = {}
	def memoized(a,b,c):
	    q = (len(a),len(b),c,a[0][0],a[0][1],b[0][0],b[0][1])
	    if q not in cache:
	        cache[q] = f(a,b,c)
	    return cache[q]
	return memoized

>>> def processInput():
	a = input()
	a = a.split('\n')
	T = int(a[0])
	a.remove(a[0])
	def largeToy(Nord,Mord):
	    answer = 0
	    while len(Nord) != 0 and len(Mord) != 0 and Nord[0][0] == Mord[0][0]:
	        if Nord[0][1] > Mord[0][1]:
	            answer += Mord[0][1]
	            Nord[0][1] -= Mord[0][1]
	            Mord.remove(Mord[0])
	        elif Nord[0][1] < Mord[0][1]:
	            answer += Nord[0][1]
	            Mord[0][1] -= Nord[0][1]
	            Nord.remove(Nord[0])
	        else:
	            answer += Nord[0][1]
	            Nord.remove(Nord[0])
	            Mord.remove(Mord[0])
	    if len(Nord) == 0 or len(Mord) == 0:
	        return answer
	    Nord2 = list()
	    Mord2 = list()
	    Nord3 = list()
	    Mord3 = list()
	    for i in Nord:
	        Nord2.append([i[0],i[1]])
	        Nord3.append([i[0],i[1]])
	    for i in Mord:
	        Mord2.append([i[0],i[1]])
	        Mord3.append([i[0],i[1]])
	    Mord3.remove(Mord3[0])
	    Nord3.remove(Nord3[0])
	    answer += max(largeToyHelper(Nord,Mord, True), largeToyHelper(Nord2,Mord2, False), largeToy(Nord3,Mord3))
	    return answer
	for i in range(1, T+1):
	    def largeToyHelper(Nord, Mord,toy):
	        answer = 0
	        Nordset = set()
	        Mordset = set()
	        if toy:
	            for i in Mord:
	                Mordset.add(i[0])
	            while len(Mord) != 0 and len(Nord) != 0 and Nord[0][0] != Mord[0][0]:
	                if Nord[0][0] not in Mordset:
	                    Nord.remove(Nord[0])
	                else:
	                    Mord.remove(Mord[0])
	        else:
	            for i in Nord:
	                Nordset.add(i[0])
	            while len(Nord) != 0 and len(Mord) != 0 and Nord[0][0] != Mord[0][0]:
	                if Mord[0][0] not in Nordset:
	                    Mord.remove(Mord[0])
	                else:
	                    Nord.remove(Nord[0])	
	        if len(Nord) == 0 or len(Mord)==0:
	            return 0
	        answer += largeToy(Nord,Mord)
	        return answer
	    largeToyHelper = memo(largeToyHelper)
	    temp = a[0].split(' ')
	    N = int(temp[0])
	    M = int(temp[1])
	    a.remove(a[0])
	    tempN = a[0].split(' ')
	    tempM = a[1].split(' ')
	    a.remove(a[0])
	    a.remove(a[0])
	    Nord = list()
	    Mord = list()
	    for m in range(N):
	        Nord.append([int(tempN[2*m+1]),int(tempN[2*m])])
	    for m in range(M):
	        Mord.append([int(tempM[2*m+1]),int(tempM[2*m])])
	    print("Case #" + str(i) + ": " + str(largeToy(Nord,Mord)))

>>> processInput()
[Paste input here, output will be printed]