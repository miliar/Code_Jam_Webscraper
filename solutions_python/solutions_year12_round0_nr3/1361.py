ncases = int(raw_input())
for k in range(0,ncases):
	A, B = raw_input().split(" ")
	A = int(A)
	B = int(B)
	count = 0
	for n in range (A,B):
		num = str(n)
		visited = []
       		for i in range(1, len(num)):
			newNum = num[i:]+num[:i]
			m = int(newNum)
			if m<=B and n<m and m not in visited:
				count = count+1
				visited.append(m)	
	print "Case #{0}: {1}".format(k+1, count)
