T = int(raw_input()) 
for t in range(T):
	inputs = raw_input().split(" ")
	s_max = int(inputs[0])
	shyness = map(int,list(inputs[1]))
	friends = 0
	stand = 0
	for i in range(s_max+1):
		if stand < i:
			friends += i - stand
			stand += i - stand
		stand += shyness[i]
	print "Case #%d: %d" % (t+1,friends)