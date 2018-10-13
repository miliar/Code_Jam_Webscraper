T = int(raw_input())
for t in range(T):
	n = int(raw_input())
	s1 = sorted([float(i) for i in raw_input().split()])
	s2 = sorted([float(i) for i in raw_input().split()])
	ss1 = s1[:]
	ss2 = s2[:]
	w1 = 0
	w2 = 0
	while (len(s1) > 0):
		if (s1[0] > s2[0]):
			s1.pop(0)
			s2.pop(0)
			w1 += 1
		else:
			s1.pop(0)
			s2.pop()
	while (len(ss1) > 0):
		if (ss1[-1] > ss2[-1]):
			ss1.pop()
			ss2.pop(0)
			w2 += 1
		else:
			ss1.pop()
			ss2.pop()
	print "Case #{}: {} {}".format(t+1, w1, w2)
