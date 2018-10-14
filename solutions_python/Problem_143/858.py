from itertools import permutations
a=int(raw_input())
for i in range(a):
	tot=0
	l=[int(x) for x in raw_input().split()]
	m=permutations(range(max(l[0],l[1])), 2)
	m2=[]
	for j in range(max(l[0],l[1])):
		m2.append((j,j))
	for j in m: 
		if (j[0]<l[0] and j[1]<l[1]):
			ans = j[0] & j[1]
			if (ans<l[2]):
				tot=tot+1
	for j in m2: 
		if (j[0]<l[0] and j[1]<l[1]):
			ans = j[0] & j[1]
			if (ans<l[2]):
				tot=tot+1
	print "Case #%d: %d" %(i+1, tot)
	

