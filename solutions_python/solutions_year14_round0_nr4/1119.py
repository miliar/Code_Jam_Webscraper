T = int(raw_input())



for tt in range(T):
	num = int(raw_input())
	ss1 = map(float, raw_input().split(" "))
	ss2 = map(float, raw_input().split(" "))
	s1 = sorted(ss1)
	s2 = sorted(ss2)
	
	a1 = 0
	for i in range(num):
		if s1[0] < s2[0]:
			s1 = s1[1:]
			s2 = s2[:-1]
		else:
			s1 = s1[1:]
			s2 = s2[1:]
			a1 += 1
	a2 = 0
	s1 = sorted(ss1)
	s2 = sorted(ss2)
	nn = num
	for i in range(num):
		for j in range(len(s2)):
			if s2[j]>s1[0]:
				s1 = s1[1:]
				s2 = s2[:j]+s2[j+1:]
				nn -= 1
				break
		
	print "Case #{0}: {1} {2}".format(str(tt+1), str(a1), str(nn))

	# C = s[0]
	# F = s[1]
	# X = s[2]
	# current = 2.0
	# cost = 0
	# while X/current+cost > buy1(C, F, X, current, cost):
	# 	cost += C/current
	# 	current += F
	# print "Case #{0}: {1}".format(str(tt+1), str(cost + X/current))
