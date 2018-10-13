def ans(l1,p1,l2,p2):
        s1 = set(l1[p1-1])
        s2 = set(l2[p2-1])
        if set(s1).isdisjoint(s2): return "Volunteer cheated!"
        else:
                inters = s1.intersection(s2)
                if len(inters)>1: return "Bad magician!"
                else: return inters.pop()
		

T = int(raw_input())
for case in range(1, T + 1):
	p1 = int(raw_input())
	l1 = []
	
	for i in range(4):
		l1.append(map(int, raw_input().split()))

	p2 = int(raw_input())
	l2 = []	
	for i in range(4):
		l2.append(map(int, raw_input().split()))

	print "Case #%d: " % (case), ans(l1,p1,l2,p2)
