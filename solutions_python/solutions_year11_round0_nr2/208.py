for casenum in xrange(1,1+int(raw_input())):
	L = [z for z in raw_input().split()]
	c = int(L[0])
	C = []
	for i in xrange(1,c+1):
		C.append([L[i][0],L[i][1],L[i][2]])
		C.append([L[i][1],L[i][0],L[i][2]])
	d = int(L[c+1])
	D = []
	for i in xrange(c+2, c+2+d):
		D.append([ L[i][0], L[i][1] ])
		D.append([ L[i][1], L[i][0] ])
	N = L[c+d+3]
	result = []
	for n in N:
		if len(result) == 0:
			result.append(n)
			continue
		flag = 0
		for c in C:
			if c[0] == n and c[1] == result[-1]:
				del result[-1:]
				result.append(c[2])
				flag = 1
				break
		if flag == 0:
			for d in D:
				if d[0] == n:
					for r in result:
						if r == d[1]:
							result = []
							flag = 1
							break
				if flag == 1:
					break
		if flag == 0:			
			result.append(n)
	ans = "["
	for x in result:
		ans += str(x) + ", "
	if len(result) != 0:
		ans = ans[:-2]
	ans += "]"	
	print ("Case #%d: " % casenum)	+ str(ans)	