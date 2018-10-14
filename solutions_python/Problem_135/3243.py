T = int(raw_input())

for n in range(T):
	a1 = int(raw_input())
	g1 = [[int(i) for i in raw_input().split()] for j in range(4)]
	r1 = set(g1[a1-1])
	a2 = int(raw_input())
	g2 = [[int(i) for i in raw_input().split()] for j in range(4)]
	r2 = set(g2[a2-1])
	
	p = r2.intersection(r1)
	
	print "Case #" + str(n+1) + ":",
	if len(p) == 1:
		print list(p)[0]
	elif len(p) > 1:
		print "Bad magician!"
	else:
		print "Volunteer cheated!"

	
