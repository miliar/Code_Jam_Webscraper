N = int(raw_input())

for p in range(N):
	r1 = int(raw_input())
	lst1 = [[int(x) for x in raw_input().split()] for i in range(4)]
	r2 = int(raw_input())
	lst2 = [[int(x) for x in raw_input().split()] for i in range(4)]
	c = list(set(lst1[r1-1]) & set(lst2[r2-1]))
	if not c: print "Case #"+str(p+1)+": Volunteer cheated!"
	elif len(c) > 1: print "Case #"+str(p+1)+": Bad magician!"
	else: print "Case #"+str(p+1)+": "+str(c[0])