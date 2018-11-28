T = input()
for _ in range(0,T):
	inp = raw_input().split(' ')
	N = int(inp[0])
	S = inp[1]
	s = 0
	ret = 0
	for i in range(0,N+1):
		if int(S[i]) != 0:
			if s < i:
				d = i-s
				ret += d
				s += d
				s += int(S[i])
			else:
				s += int(S[i])
	print "Case #" + str(_+1) + ": " + str(ret)

